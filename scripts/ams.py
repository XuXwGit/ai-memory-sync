#!/usr/bin/env python3
"""Offline, non-destructive portable-context prototype. Never contacts a service."""
import argparse
from datetime import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

VERSION = '0.1.0'
KINDS = ('memory', 'project', 'task', 'conversation', 'config', 'automation')
SCHEMA = Path(__file__).resolve().parents[1] / 'schemas' / 'v1'

class Invalid(ValueError):
    pass

def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n'

def load(path):
    p = Path(path)
    if p.is_symlink() or not p.is_file():
        raise Invalid('Input must be a regular non-symlink JSON file')
    if p.stat().st_size > 10_000_000:
        raise Invalid('Input exceeds the 10 MB prototype limit')
    return json.loads(p.read_text(encoding='utf-8'))

def scan(value):
    """Conservative blocking heuristics; never log the matched value."""
    findings = []
    forbidden = re.compile(r'^(password|passwd|token|access_token|refresh_token|api_key|client_secret|session_token|secret|private_key|verification_code|recovery_code|cookie|authorization)$', re.I)
    patterns = [
        ('possible-phone', re.compile(r'(?<![\w])(?:\+\d[\d ()-]{8,}\d|1[3-9]\d{9})(?![\w])')),
        ('auth-header', re.compile(r'(?:authorization\s*:\s*bearer\s+\S+|cookie\s*:\s*\S+)', re.I)),
        ('private-key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
        ('credential-pattern', re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b')),
        ('credential-assignment', re.compile(r'(?:password|api[_ -]?key|access[_ -]?token|secret)\s*[:=]\s*\S+', re.I)),
        ('sensitive-url', re.compile(r'https?://[^\s]*(?:[?&](?:token|key|secret|code)=|/subscribe\b)', re.I)),
    ]
    def walk(v, path='$'):
        if isinstance(v, dict):
            for k, x in v.items():
                if forbidden.match(k) and x not in (None, '', '[REDACTED]'):
                    findings.append({'path':path, 'rule':'credential-field'})
                walk(x, path + '.' + k)
        elif isinstance(v, list):
            for i, x in enumerate(v): walk(x, path + '[' + str(i) + ']')
        elif isinstance(v, str):
            for name, pat in patterns:
                if pat.search(v): findings.append({'path':path, 'rule':name})
    walk(value)
    # Paths themselves can contain hostile keys, so results expose no raw keys or values.
    return [{'finding':i+1, 'rule':f['rule']} for i, f in enumerate(findings)]

def schema_check(obj, name):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        raise Invalid('Install the declared jsonschema dependency to validate; no operation performed')
    schema = json.loads((SCHEMA / (name + '.schema.json')).read_text())
    errs = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(obj))
    if errs:
        # Do not echo input or schema exception text, which may contain a secret.
        raise Invalid(f'{name} schema failed ({len(errs)} issue(s)); inspect input locally')

def validate_records(records):
    if not isinstance(records, list): raise Invalid('records must be an array')
    seen = set()
    for item in records:
        if not isinstance(item, dict) or item.get('kind') not in KINDS: raise Invalid('Unknown record kind')
        schema_check(item, item['kind'])
        try:
            timestamp = item['updated_at']
            if timestamp is not None and ('T' not in timestamp or datetime.fromisoformat(timestamp.replace('Z', '+00:00')).tzinfo is None):
                raise ValueError()
        except ValueError:
            raise Invalid('updated_at must be an ISO timestamp with timezone')
        key = (item['source_account'], item['id'])
        if key in seen: raise Invalid('Duplicate record identity')
        seen.add(key)
    findings = scan(records)
    if findings: raise Invalid(f'Secret scan blocked {len(findings)} finding(s); no output created')

def pack(source, target):
    records = load(source)
    validate_records(records)
    target = Path(target)
    if target.exists(): raise Invalid('Destination already exists; source and existing outputs are preserved')
    data = dumps(records).encode()
    manifest = {'format_version':'1.0', 'producer_version':VERSION, 'file':'records.json',
                'sha256':hashlib.sha256(data).hexdigest(), 'record_count':len(records),
                'coverage':'selected_records_only', 'exclusions':['hidden_platform_state'], 'privacy_review':'required',
                'scan_status':'no_heuristic_findings_not_a_guarantee',
                'restore_mode':'reference_context', 'native_import_verified':False}
    schema_check(manifest, 'manifest')
    target.mkdir(parents=True, exist_ok=False, mode=0o700)
    try:
        for filename, content in [('records.json', data), ('manifest.json', dumps(manifest).encode())]:
            fd = os.open(target / filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, 'wb') as handle:
                handle.write(content)
    except Exception:
        raise Invalid('Package write interrupted; validate before use, do not treat as complete')
    return {'status':'packaged_locally', 'record_count':len(records), 'network_actions':0,
            'native_import_verified':False}

def validate(package):
    root = Path(package)
    if root.is_symlink() or not root.is_dir(): raise Invalid('Package must be a non-symlink directory')
    if set(x.name for x in root.iterdir()) != {'manifest.json','records.json'}:
        raise Invalid('Package must contain exactly manifest.json and records.json')
    manifest = load(root / 'manifest.json')
    schema_check(manifest, 'manifest')
    records = load(root / 'records.json')
    validate_records(records)
    raw = (root / 'records.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != manifest['sha256']: raise Invalid('Checksum mismatch')
    if len(records) != manifest['record_count']: raise Invalid('Record count mismatch')
    return records

def preview(package, destination, scopes):
    records = validate(package)
    selected = [r for r in records if r['scope'] in scopes and r['explicit']]
    return {'status':'preview_only', 'destination':destination, 'included_count':len(selected),
            'excluded_count':len(records)-len(selected), 'native_import_verified':False,
            'items':[{'id':r['id'], 'source_account':r['source_account'], 'kind':r['kind'],
                      'action':'reference_context_only'} for r in selected],
            'requires':['destination authorization', 'content review', 'platform capability check'],
            'automations_enabled':False, 'credentials_transferred':False,
            'warning':'Preview does not filter the source package. Do not share the package as a selected subset.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command', required=True)
    p=sub.add_parser('scan'); p.add_argument('input')
    p=sub.add_parser('pack'); p.add_argument('input'); p.add_argument('output')
    p=sub.add_parser('validate'); p.add_argument('package')
    p=sub.add_parser('preview'); p.add_argument('package'); p.add_argument('--destination', required=True); p.add_argument('--scope', action='append', choices=['shared','account_only'], default=None)
    a=parser.parse_args()
    try:
        if a.command=='scan':
            findings=scan(load(a.input)); result={'status':'blocked' if findings else 'no_heuristic_findings','findings':findings,'guarantee_of_safety':False}
            print(dumps(result), end=''); return 2 if findings else 0
        elif a.command=='pack': result=pack(a.input,a.output)
        elif a.command=='validate': result={'status':'valid_local_package','record_count':len(validate(a.package)), 'native_import_verified':False}
        else: result=preview(a.package,a.destination,a.scope or ['shared'])
        print(dumps(result), end=''); return 0
    except (Invalid, OSError, ValueError, KeyError, TypeError):
        # Safe errors only; never echo raw parser failures or secret-bearing data.
        print('Operation stopped: invalid input, failed integrity/security check, missing dependency, or inaccessible path. No remote action was taken.', file=sys.stderr)
        return 2

if __name__=='__main__': sys.exit(main())
