# 两分钟体验

## 不安装，不连接账号

1. 打开 START.md，把提示词复制进任意 AI 的新会话。
2. 在末尾补一句：**直接演示跨账号迁移，只用虚构数据，不连接任何真实账号。**
3. 看它能否给出备份范围、目的账号、迁移预览和未支持项，而不是声称已写入原生记忆。
4. 选择一条虚构偏好和一个虚构待办，把 AI 生成的恢复上下文复制到另一个账号的新会话。
5. 问新 AI：**我的回复偏好是什么？下一项待办是什么？你是从当前文件得知，还是已经保存为长期记忆？**

这一步检验的是上下文可理解性，不是原生记忆、定时同步或历史聊天完整恢复。

## 可选：运行确定性本地测试

要求 Python 3.10+，安装 requirements.txt 中依赖后，在仓库目录运行：

```sh
python scripts/ams.py scan examples/records.json
python scripts/ams.py validate examples/sample-backup
python scripts/ams.py preview examples/sample-backup --destination demo-account-b
python -m unittest discover -s tests -v
```

预期：备份含 6 条虚构记录；默认迁移预览含 5 条 shared 记录，排除 1 条 account_only 会话。自动化不启用，真实账号不修改。

## 给维护者的反馈

请只分享平台名称、能力缺口、错误消息和虚构复现数据。不要提交真实会话、凭据、个人备份或包含私人内容的截图。
