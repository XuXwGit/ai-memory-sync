import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ams',ROOT/'scripts/ams.py');ams=importlib.util.module_from_spec(spec);spec.loader.exec_module(ams)
class CoreTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);self.records=json.loads((ROOT/'examples/records.json').read_text());self.source=self.root/'in.json';self.save()
 def tearDown(self):self.temp.cleanup()
 def save(self):self.source.write_text(json.dumps(self.records))
 def package(self):ams.pack(self.source,self.root/'package');return self.root/'package'
 def test_private_modes(self):
  p=self.package();self.assertEqual(p.stat().st_mode & 0o777,0o700)
  for f in p.iterdir():self.assertEqual(f.stat().st_mode & 0o777,0o600)
 def test_auth_headers(self):
  for value in ['Authorization: Bearer synthetic','Cookie: sessionid=synthetic']:
   self.assertTrue(ams.scan(value))
  self.assertTrue(ams.scan({'client_secret':'synthetic'}))
 def test_roundtrip(self):self.assertEqual(ams.validate(self.package()),self.records)
 def test_default_scope(self):
  p=ams.preview(self.package(),'account-b',['shared']);self.assertEqual(p['included_count'],5);self.assertEqual(p['excluded_count'],1);ams.schema_check(p,'receipt')
 def test_inferred_excluded(self):
  self.records[0]['explicit']=False;self.save();self.assertEqual(ams.preview(self.package(),'b',['shared'])['included_count'],4)
 def test_explicit_account_scope(self):self.assertEqual(ams.preview(self.package(),'account-b',['account_only'])['included_count'],1)
 def test_preserve_existing(self):
  p=self.package();before=(p/'records.json').read_bytes()
  with self.assertRaises(ams.Invalid):ams.pack(self.source,p)
  self.assertEqual(before,(p/'records.json').read_bytes())
 def test_checksum(self):
  p=self.package();(p/'records.json').write_text(ams.dumps(self.records)+' ')
  with self.assertRaises(ams.Invalid):ams.validate(p)
 def test_duplicate(self):
  self.records.append(copy.deepcopy(self.records[0]));self.save()
  with self.assertRaises(ams.Invalid):self.package()
 def test_cross_account_identity(self):
  r=copy.deepcopy(self.records[0]);r['source_account']='another';self.records.append(r);self.save();self.assertEqual(len(ams.validate(self.package())),7)
 def test_unknown_kind(self):
  self.records[0]['kind']='unknown';self.save()
  with self.assertRaises(ams.Invalid):self.package()
 def test_unknown_timestamp(self):
  self.records[0]['updated_at']=None;self.save();self.assertIsNone(ams.validate(self.package())[0]['updated_at'])
 def test_invalid_timestamp(self):
  self.records[0]['updated_at']='yesterday';self.save()
  with self.assertRaises(ams.Invalid):self.package()
 def test_secret_field(self):
  self.records[4]['data']['settings']['token']='not-a-real-token';self.save()
  with self.assertRaises(ams.Invalid):self.package()
  self.assertFalse((self.root/'package').exists())
 def test_secret_text(self):
  self.records[0]['data']['text']='password=synthetic-test';self.save()
  with self.assertRaises(ams.Invalid):self.package()
 def test_scan_never_echoes_values(self):self.assertNotIn('synthetic-secret',json.dumps(ams.scan({'token':'synthetic-secret'})))
 def test_phone(self):self.assertTrue(ams.scan('+1 202 555 0123'))
 def test_private_key(self):self.assertTrue(ams.scan('-----BEGIN PRIVATE KEY-----'))
 def test_credential_url(self):self.assertTrue(ams.scan('https://example.invalid/path?token=demo'))
 def test_symlink(self):
  link=self.root/'link.json';link.symlink_to(self.source)
  with self.assertRaises(ams.Invalid):ams.load(link)
 def test_package_extra_file(self):
  p=self.package();(p/'unreviewed.txt').write_text('extra')
  with self.assertRaises(ams.Invalid):ams.validate(p)
 def test_manifest_path_traversal(self):
  p=self.package();m=ams.load(p/'manifest.json');m['file']='../outside';(p/'manifest.json').write_text(ams.dumps(m))
  with self.assertRaises(ams.Invalid):ams.validate(p)
 def test_no_activation(self):
  self.records[5]['data']['enabled_on_destination']=True;self.save()
  with self.assertRaises(ams.Invalid):self.package()
 def test_preview_is_nonmutating(self):
  p=self.package();before={x.name:x.read_bytes() for x in p.iterdir()};ams.preview(p,'demo-b',['shared']);self.assertEqual(before,{x.name:x.read_bytes() for x in p.iterdir()})
 def test_schema_validity(self):
  from jsonschema import Draft202012Validator
  for p in (ROOT/'schemas/v1').glob('*.json'):Draft202012Validator.check_schema(json.loads(p.read_text()))
if __name__=='__main__':unittest.main()
