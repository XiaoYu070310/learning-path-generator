# learning-path-generator

`learning-path-generator` is an agent skill for creating structured, local learning-material packages for almost any subject. It turns requests such as "I want to learn C++", "help me prepare for CET-4", or "make an HPC study kit" into an ordered set of files with a roadmap, phase guides, resource indexes, practice specifications, acceptance criteria, and review guidance.

The skill is based on a simple principle: learning materials should lead to learner-owned practice, not replace it.

## What it generates

A typical package contains:

```text
topic-learning-package/
|-- 00_先看我_[主题]学习总图.md
|-- 01_资料使用顺序.md
|-- 02_学习环境与工具.md
|-- 03_学习计划与阶段验收.md
|-- references/
|-- books/
|-- tools/          # optional
|-- projects/       # empty, for the learner
`-- journal/        # empty, for the learner
```

The exact files adapt to the subject. A C++ package emphasizes code, builds, debugging, and tests. An English-exam package emphasizes diagnosis, vocabulary in context, listening, reading, writing, simulations, and error analysis.

## Important boundary

`projects/` and `journal/` must remain empty. They are reserved for the learner's own work. The skill does not pre-fill exercises, solutions, code, logs, fake results, or reflections there.

Git cannot track empty directories. If a generated package is committed to GitHub, create these directories locally after cloning. This repository intentionally does not recommend `.gitkeep` for them because that would make them non-empty.

## Installation

Install or copy this repository as a skill directory recognized by your agent. The repository root is the skill root and contains `SKILL.md` directly.

## Example prompts

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

## Repository structure

```text
SKILL.md                  Core agent workflow
references/               Detailed architecture and quality rules
assets/                   Adaptable Markdown templates
scripts/                  Package validator
evals/                    Representative evaluation prompts
LICENSE                    MIT License
```

## Validate a generated package

```bash
python scripts/validate_learning_package.py path/to/topic-learning-package
```

The validator checks required navigation files, Markdown links, accidental personal paths, unwanted binaries, unresolved placeholders, and whether `projects/` and `journal/` are truly empty.

## Scope

Use this skill to create a substantial curriculum or supporting file package. It is not intended for answering one isolated question, solving one exercise, or recommending a single book.

## License

MIT
