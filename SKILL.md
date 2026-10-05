---
name: learning-path-generator
description: Create complete, local learning-material packages for any subject, including staged roadmaps, ordered guides, setup instructions, references, practice specifications, acceptance criteria, and review guidance. Use this skill whenever a user asks AI to make files, a folder, a curriculum, a self-study kit, or supporting materials for learning a field such as C++, HPC, English exams, mathematics, science, professional skills, or another substantial topic. Also use it for requests like "我要学习某领域，帮我制作学习文件/资料包/路线" even when the user does not mention this skill. Do not use it for answering one isolated knowledge question, solving one exercise, or recommending only one resource.
---

# Learning Path Generator

Create a coherent learning system, not a pile of notes. The learner should know where to start, what to do, how to verify progress, and what to postpone.

## Core outcome

Generate a self-contained directory of learning-support files tailored to the learner and subject. Separate authored guidance from learner-owned work:

- Put explanations, roadmaps, task specifications, resource indexes, and acceptance criteria in the generated documents.
- Create `projects/`, `journal/`, and `notes/` as empty directories.
- Never place exercises, starter code, answers, sample projects, experiment results, logs, review entries, notes, `.gitkeep`, or any other file in those three directories.
- Do not copy personal work from a source package into the output.
- Include an `AGENTS.md` tutor specification so any AI session opened in this folder continues teaching coherently (see step 5).

If the user's requested output location is unknown and files must be created, ask one short location question. Infer non-critical details when reasonable and record those assumptions in the overview instead of conducting a long interview.

## Workflow

### 1. Understand the learner

Extract what is already known from the request and conversation:

- subject and intended scope;
- current level and relevant background;
- goal: exam, competition, employment, research, project, or interest;
- available time and deadline;
- platform, tools, language, and accessibility constraints;
- desired depth and preferred learning style.

When details are absent, use conservative defaults: beginner level, sustainable part-time study, free/legal resources, and a route that can be shortened or extended. State assumptions in `00_先看我_[主题]学习总图.md`.

### 2. Classify the domain

Choose an appropriate learning model before designing files. Read `references/domain-adaptation.md` for domain-specific requirements.

- Programming/engineering: correctness, environment, debugging, tests, progressively larger implementations.
- Exam/language: diagnosis, skill modules, deliberate practice, timed simulation, error review.
- Mathematics/theory: prerequisites, definitions, worked understanding, proof/problem practice, cumulative checks.
- Practical/professional: concepts, tools, realistic deliverables, critique, portfolio evidence.
- Mixed/interdisciplinary: identify the prerequisite spine and keep application tracks optional until foundations are ready.

Do not mechanically transfer programming conventions into unrelated subjects.

### 3. Research only when needed

Research current facts before writing when the package depends on changing information: exam syllabi, competition rules, software versions, installation commands, official course URLs, certifications, or admissions requirements.

- Prefer official sources, then reputable open educational resources.
- Record source title, URL, purpose, and access date in the relevant resource index.
- Never invent a URL, version, policy, score threshold, or course title.
- If internet access is unavailable, omit unverified specifics and mark what the learner must verify.
- Do not download or redistribute copyrighted books, paid courses, leaked exams, or proprietary files. Link to lawful sources instead.

Stable conceptual material does not require web research merely to add citations.

### 4. Design backward from the goal

Define the final capability first, then prerequisites and phases. Each phase needs:

1. entry requirements;
2. concrete capability goal;
3. essential concepts only;
4. learning resources and how to use them;
5. learner-owned practice tasks;
6. observable acceptance criteria;
7. common mistakes and recovery advice;
8. exit condition for the next phase.

Use artifacts and demonstrated capability as evidence. Watching hours, page counts, streaks, and commit counts are activity measures, not primary acceptance criteria.

### 5. Build the package

Follow `references/output-architecture.md` and `references/content-standards.md`. Use templates in `assets/` as structural prompts, adapting or omitting sections that do not fit.

Default package:

```text
[topic-learning-package]/
|-- AGENTS.md              # tutor specification, adapted from assets/agents-md-template.md
|-- 00_先看我_[主题]学习总图.md
|-- 01_资料使用顺序.md
|-- 02_学习环境与工具.md
|-- 03_学习计划与阶段验收.md
|-- references/
|   |-- 00_完整学习路线.md
|   |-- 01_[基础主题].md
|   |-- ...
|   |-- 80_成果与作品集建设.md
|   `-- 82_周复盘说明.md
|-- books/
|   `-- 00_书籍与长资料阅读顺序.md
|-- tools/                 # only when useful
|-- notes/                 # empty; filled by the AI tutor during teaching
|-- projects/              # empty
`-- journal/               # empty
```

This is a flexible architecture, not a quota. Keep useful files and omit empty decorative sections. Do not create `apps/`, installers, archives, binaries, generated websites, or dashboards unless the user explicitly requests them and they improve learning.

### Tutor specification (AGENTS.md)

`AGENTS.md` turns the package into a long-running tutoring workspace. Any AI session opened in the folder reads it first, so teaching continues from the recorded state instead of starting over. Build it from `assets/agents-md-template.md`, rewritten in the learner's language for this subject, learner, and machine. It must cover:

1. role and the final capability goal;
2. the pre-lesson checklist: read the teaching journal, confirm the current phase and blockers, and do not re-teach mastered content;
3. teaching basis: which files define the route, with an explicit instruction to adapt them rather than follow mechanically;
4. teaching method: one concept at a time, reasons before examples, the learner does the work, every claim verified through real practice in the domain — executing, solving, producing, or measuring — with verified correctness before speed or polish, and environment limits stated plainly;
5. the `notes/` system: what is worth recording, block-based file naming, the review-note writing standard, and the historical backfill rule;
6. the `journal/` progress log: file name, entry template, and the distinction between taught, learner-written, and verified;
7. directory responsibilities and the learner's environment constraints.

Fill the environment section from what setup and diagnosis actually established — available tools, practical limits, and constraints the learner states. Never invent specifications. Omit or reword sections that do not fit the domain, but keep the notes and journal rules: they are what make progress survive across sessions.

### 6. Check the package

Read `references/quality-checklist.md`, then run:

```bash
python scripts/validate_learning_package.py <generated-package-path>
```

When this skill is installed elsewhere, resolve the script relative to this skill's directory. Fix all errors before reporting completion. Warnings require review but may be justified by the domain.

Also manually verify:

- the first action is possible today;
- links and commands match the declared platform;
- phases do not assume knowledge introduced later;
- main and optional tracks are visibly separated;
- exercises specify goals and checks without supplying the learner's completed work;
- `projects/`, `journal/`, and `notes/` are present and completely empty;
- the `AGENTS.md` is adapted to this learner and free of unresolved placeholders.

## Naming and navigation

Use ordered two-digit prefixes. Recommended ranges:

```text
00-09  orientation and prerequisites
10-19  core beginner material
20-29  intermediate capability
30-39  advanced practice or real-world work
40-49  optional tracks
50-79  official references and lookup guides
80-89  portfolio, review, and long-term development
```

Do not fill every range. Use relative links. Keep overview documents concise and link to detailed documents rather than duplicating them.

## Writing rules

- Match the user's language; for Chinese users, write natural Chinese and preserve useful English terminology.
- Explain why a task matters and what evidence demonstrates completion.
- Prefer short experiments and feedback loops before large projects.
- Distinguish facts, recommendations, estimates, and assumptions.
- Qualify platform-dependent commands and performance claims.
- Include correctness, safety, ethics, or legal checks where relevant.
- Avoid exaggerated promises, fake precision, gamified titles, and generic motivational filler.
- Do not claim an environment was installed, a command was tested, or a link was checked unless it actually was.
- Do not write absolute personal paths into reusable files.
- Do not embed personal names, credentials, tokens, private data, or source-package training records.

## Empty learner directories

`projects/`, `journal/`, and `notes/` stay empty at generation time, but they are not all learner-authored — `AGENTS.md` defines who writes what after generation:

- `projects/` belongs exclusively to the learner.
- `notes/` becomes the learner's long-term review material, written by the AI tutor as study blocks are completed.
- `journal/` holds the tutor's teaching progress log and later review summaries.

Keep all three empty even if examples would be convenient. Put task descriptions in `references/` and the writing rules in `AGENTS.md`, not in these directories. Do not add sample notes, progress entries, README files, or `.gitkeep`.

Git does not track empty directories. If the generated package itself will be committed, explain in its README or final response that the learner should create these directories after cloning. Do not add placeholder files unless the user explicitly overrides the empty-directory rule.

## Completion report

After generation, report concisely:

- output path;
- learner profile and assumptions used;
- phase outline;
- whether current information was researched and from where;
- validation result;
- confirmation that `projects/`, `journal/`, and `notes/` are empty;
- what the `AGENTS.md` specification fixes as the teaching role, notes rules, and environment constraints;
- the exact first file and first action to begin with.
