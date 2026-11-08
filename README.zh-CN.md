# AI Memory Sync

AI Memory Sync 是一个以提示词为入口、与平台无关的实验性 MVP。它把你**主动提供或明确授权读取**的信息整理成可移植、可审阅的上下文包。直接把 [`START.md`](START.md) 全文复制到任意 AI 对话即可开始，不需要安装软件，也不要求平台支持 Skill。

MVP 处理六类用户数据：

- 记忆与偏好
- 对话与摘要
- 项目
- 任务
- 用户可见配置
- 自动化定义

它不会假装能读取平台隐藏记忆、内部状态、未提供的历史对话或其他不可访问数据。密码、令牌、私钥、恢复码、支付信息等秘密必须排除。

## 两分钟试用

先看 [TRY-ME.md](TRY-ME.md)。最短体验：把 START.md 贴到新会话，补一句“直接演示跨账号迁移，只用虚构数据，不连接真实账号”。

## 五分钟开始

1. 打开 [`START.md`](START.md)，复制全文到目标 AI。
2. 选择 `demo`，用纯合成数据体验；或选择 `real`，使用你提供或授权读取的数据。
3. 选择流程：`backup`、`restore`、`migrate`、`sync` 或 `config-migration`。
4. 先审阅范围、排除项、能力报告和任何上传目标，再决定是否授权。
5. 把生成的可移植包保存到你控制的位置。有效 v1 包只包含 `manifest.json` 和 `records.json`。

真实备份优先使用官方导出或你上传的文件。原始导出应保持不变；规范化后的包是派生物，不能替代原始来源。

## MVP 中“同步”的含义

当前的同步是：比较用户提供的包、提出变更、解决冲突并生成下一版待审阅包。它不代表无人值守的跨平台双向同步。配套本地 CLI 只负责本地打包、校验和预览，不会实际上传 GitHub、写入平台原生记忆、创建定时任务或修改远端账户。

## 可选本地校验器

复制提示词无需安装。可选 CLI 需要 Python 和项目声明的 `jsonschema` 依赖，只在本地工作，不上传、不原生导入、不修改账户。

```bash
python scripts/ams.py scan INPUT.json
python scripts/ams.py pack INPUT.json OUTPUT_DIR
python scripts/ams.py validate PACKAGE_DIR
python scripts/ams.py preview PACKAGE_DIR --destination DESTINATION_ALIAS
python scripts/ams.py preview PACKAGE_DIR --destination DESTINATION_ALIAS --scope shared --scope account_only
```

`scan` 只是启发式检查，不能保证绝对安全。`pack` 接受符合 Schema 的 JSON 数组，并拒绝覆盖已有输出目录。`validate` 要求目录内恰好有 `manifest.json` 和 `records.json`，再检查 Schema、记录数、秘密扫描与校验和。`preview` 只读，默认只选 `shared`；审阅账户专属内容后才能同时加入两个 `--scope`。

## 目录

- [`START.md`](START.md)：中文为主、可独立复制的入口提示词
- [`prompts/core.md`](prompts/core.md)：通用行为约定
- [`prompts/flows/`](prompts/flows)：各流程提示词
- [`adapters/`](adapters)：运行时能力检查与平台说明
- [`skills/ai-memory-sync/SKILL.md`](skills/ai-memory-sync/SKILL.md)：可选 Skill 包装
- [`docs/`](docs)：架构、协议、隐私、恢复与路线图

## 存储与分享

公开项目仓库只应放代码、提示词、文档、Schema 和合成示例。真实用户数据应放在另一个私有位置或私有仓库。私有仓库只能降低暴露风险，不能让上传自动变得安全。任何上传前，都要确认目标、文件、账户或工作区以及分享范围。不要把凭据放进包或提示词。

## 当前状态

这是实验性 MVP。Demo 模式完全使用合成数据。真实平台操作尚未完成端到端测试，adapter 文档也不代表某个账户当前一定具备对应能力。运行时必须把所需能力标为 `已验证`、`不可用`、`未知` 或 `需要用户操作`，没有证据就不能宣称完成。


Privacy note: `preview --scope` filters the report only, not the underlying package. Never upload that original package as if unselected records were removed. Build a separate package from only the approved records for sharing. A valid package means format/integrity checks passed; `privacy_review=required` remains in the manifest. Secret scanning is heuristic, not a privacy clearance.
