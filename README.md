# learning-path-generator

[![skills.sh](https://skills.sh/b/XiaoYu070310/learning-path-generator)](https://skills.sh/XiaoYu070310/learning-path-generator)

[中文](#中文) | [English](#english)

## 中文

`learning-path-generator` 是一个用于生成结构化本地学习资料包的 Agent Skill，适用于初学者或者进阶学习。它可以把“我想学习 C++”“帮我准备英语四级”或“制作一套 HPC 学习资料”等请求，转换成一组有明确顺序的学习文件，其中包括学习路线、阶段指南、资源索引、实践任务说明、验收标准和复盘方法，但是建议的食用方式是详细的描述你的学习目标，学习时长，已经掌握的内容等以便更个性化定制你的学习路线。

这个 Skill 遵循一个简单原则：学习资料应该引导学习者亲自实践，而不是代替学习者完成训练。

### 生成内容

典型的学习资料包结构如下：

```text
主题学习资料包/
|-- 00_先看我_[主题]学习总图.md
|-- 01_资料使用顺序.md
|-- 02_学习环境与工具.md
|-- 03_学习计划与阶段验收.md
|-- references/
|-- books/
|-- tools/          # 可选
|-- projects/       # 保持为空，留给学习者实践
`-- journal/        # 保持为空，留给学习者复盘
```

具体文件会根据学习领域自动调整。例如，C++ 学习资料会重点覆盖代码、编译、调试和测试；

### 重要边界

`projects/` 和 `journal/` 必须保持为空。这两个目录只用于保存学习者自己完成的项目和复盘。Skill 不会在其中预先放入练习、答案、代码、日志、虚假结果或代写复盘。

Git 无法跟踪空目录。如果生成的学习资料包需要提交到 GitHub，请在克隆后由学习者自行创建这两个目录。本项目不建议使用 `.gitkeep`，因为这会使目录不再为空。

### 安装方法

#### 一行安装（推荐）

需要先安装 Node.js，并确保可以使用 `npx`。安装程序会检测本机支持的 Agent，并让你选择目标 Agent 和安装范围：

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator
```

以非交互方式全局安装到 OpenCode：

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator -g -a opencode -y
```

全局安装到 Claude Code：

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator -g -a claude-code -y
```

#### 让 Agent 自动安装

将下面的内容发送给具有终端和文件系统权限的 Agent：

```text
请帮我检查并自动安装这个 Agent Skill：
https://github.com/XiaoYu070310/learning-path-generator

请安装到当前 Agent 的用户级 skills 目录，安装后验证 SKILL.md 可以读取，并告诉我是否需要重启 Agent。
```

安装第三方 Skill 前应先检查其内容。对于这个公开仓库，Agent 只需要将仓库克隆或链接到官方规定的 skills 目录，不应向你索要 GitHub 密码、API Key 或 Token。

#### 手动克隆

Claude Code：

```bash
git clone https://github.com/XiaoYu070310/learning-path-generator.git ~/.claude/skills/learning-path-generator
```

OpenCode：

```bash
git clone https://github.com/XiaoYu070310/learning-path-generator.git ~/.config/opencode/skills/learning-path-generator
```

Windows 用户可以在 PowerShell 中执行相同命令。如果 Agent 启动时对应的顶层 skills 目录还不存在，安装完成后建议重启一次 Agent。

#### 更新 Skill

通过 `skills` CLI 管理的安装可以使用下面的命令更新：

```bash
npx skills update learning-path-generator
```

如果使用手动克隆方式安装，请进入已安装的 Skill 目录并执行 `git pull`。

本仓库的根目录就是 Skill 根目录，`SKILL.md` 直接位于仓库根目录。项目遵循 Agent Skills 格式，可以被 `skills` CLI、CC Switch、OpenCode、Claude Code 及其他兼容 Agent 识别。

### 使用示例

```text
我是大一学生，只会一点 Python。帮我制作一套学习 C++ 的文件，放到 D:\study\cpp。
```

```text
我要参加超算竞赛，使用 Windows 11 和 WSL。请生成一套 HPC 学习资料。
```

```text
两个月后考英语四级，每天能学 90 分钟。帮我制作一个本地学习资料包。
```

```text
我以后想学机器学习，现在需要系统补线性代数。请生成分阶段学习文件。
```

### 仓库结构

```text
SKILL.md                  Agent 核心工作流程
references/               详细的架构、内容和质量规范
assets/                   可按领域调整的 Markdown 模板
scripts/                  学习资料包验证脚本
evals/                    代表性评测提示词
LICENSE                   MIT 许可证
```

### 验证生成的学习资料包

```bash
python scripts/validate_learning_package.py path/to/topic-learning-package
```

验证器会检查必需的导航文件、Markdown 相对链接、意外写入的个人路径、不需要的二进制文件、未替换的模板占位符，以及 `projects/` 和 `journal/` 是否真正保持为空。

### 适用范围

这个 Skill 适合创建完整的学习路线或配套学习文件，不适合仅回答一个独立知识点、解决一道练习题或只推荐一本书。

### 许可证

MIT

## English(Translated by AI)

`learning-path-generator` is an Agent Skill that creates structured, local learning-material packages for both beginners and advanced learners. It turns requests such as “I want to learn C++,” “help me prepare for CET-4,” or “make an HPC study kit” into an ordered set of files containing a roadmap, phase guides, resource indexes, practice specifications, acceptance criteria, and review guidance. For the best results, describe your learning goals, available study time, and existing knowledge in detail so the generated learning path can be tailored to you.

This Skill follows one simple principle: learning materials should guide learners through their own practice rather than complete the training for them.

### What It Generates

A typical learning package has this structure:

```text
topic-learning-package/
|-- 00_先看我_[主题]学习总图.md
|-- 01_资料使用顺序.md
|-- 02_学习环境与工具.md
|-- 03_学习计划与阶段验收.md
|-- references/
|-- books/
|-- tools/          # optional
|-- projects/       # kept empty for learner practice
`-- journal/        # kept empty for learner reviews
```

The exact files adapt to the learning domain. For example, a C++ package emphasizes coding, compilation, debugging, and testing.

### Important Boundary

`projects/` and `journal/` must remain empty. These directories are reserved for projects and reviews created by the learner. The Skill does not pre-fill them with exercises, answers, code, logs, fabricated results, or ghostwritten reflections.

Git cannot track empty directories. If a generated learning package is committed to GitHub, the learner should create these directories after cloning. This project intentionally does not recommend `.gitkeep`, because it would make the directories non-empty.

### Installation

#### One-Line Install (Recommended)

Install Node.js first and make sure `npx` is available. The installer detects supported agents and lets you choose the target agent and installation scope:

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator
```

Install globally to OpenCode without interactive prompts:

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator -g -a opencode -y
```

Install globally to Claude Code:

```bash
npx skills add https://github.com/XiaoYu070310/learning-path-generator -g -a claude-code -y
```

#### Ask an Agent to Install It

Send the following instruction to an agent with terminal and filesystem access:

```text
Please inspect and automatically install this Agent Skill:
https://github.com/XiaoYu070310/learning-path-generator

Install it in the current agent's user-level skills directory, verify that SKILL.md is readable after installation, and tell me whether the agent needs to be restarted.
```

Review third-party Skills before installation. For this public repository, the agent only needs to clone or link the repository into the documented skills directory. It should not request your GitHub password, API key, or token.

#### Manual Clone

Claude Code:

```bash
git clone https://github.com/XiaoYu070310/learning-path-generator.git ~/.claude/skills/learning-path-generator
```

OpenCode:

```bash
git clone https://github.com/XiaoYu070310/learning-path-generator.git ~/.config/opencode/skills/learning-path-generator
```

Windows users can run the same commands in PowerShell. If the agent was already running when its top-level skills directory was first created, restart the agent after installation.

#### Update the Skill

Installations managed by the `skills` CLI can be updated with:

```bash
npx skills update learning-path-generator
```

For a manual clone, enter the installed Skill directory and run `git pull`.

The repository root is also the Skill root, with `SKILL.md` located directly at the top level. The project follows the Agent Skills format and can be discovered by the `skills` CLI, CC Switch, OpenCode, Claude Code, and other compatible agents.

### Example Prompts

```text
I am a first-year university student and only know a little Python. Create a set of files for learning C++ and save them to D:\study\cpp.
```

```text
I want to participate in an HPC competition and use Windows 11 with WSL. Generate a structured HPC learning package for me.
```

```text
I will take CET-4 in two months and can study for 90 minutes per day. Create a local study package for me.
```

```text
I plan to study machine learning, but first I need to learn linear algebra systematically. Generate a staged learning package for me.
```

### Repository Structure

```text
SKILL.md                  Core agent workflow
references/               Detailed architecture, content, and quality rules
assets/                   Adaptable Markdown templates
scripts/                  Learning-package validator
evals/                    Representative evaluation prompts
LICENSE                   MIT License
```

### Validate a Generated Learning Package

```bash
python scripts/validate_learning_package.py path/to/topic-learning-package
```

The validator checks required navigation files, relative Markdown links, accidental personal paths, unwanted binary files, unresolved template placeholders, and whether `projects/` and `journal/` are truly empty.

### Scope

This Skill is intended for creating complete learning paths or supporting file packages. It is not intended for answering one isolated question, solving a single exercise, or recommending only one book.

### License

MIT
