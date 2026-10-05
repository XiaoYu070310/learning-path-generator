# Output Architecture

Use this architecture to make a learning package navigable without turning every package into the same subject with renamed headings.

## Root documents

### `00_先看我_[主题]学习总图.md`

This is the learner's entry point. Include:

- intended learner and explicit assumptions;
- the final capability in plain language;
- one-line progression;
- a phase table with time estimates and observable outcomes;
- strengths and likely gaps based on the learner profile;
- the first 7 days or first 30 days;
- what to postpone and why;
- core learning principles;
- today's first action.

Keep it orienting rather than encyclopedic. Link to details.

### `01_资料使用顺序.md`

Answer one question: what should be read or used, and when?

- Group files by phase.
- Mark each item as required, optional, or lookup-only.
- Explain how to consume each resource: read fully, skim, follow along, or consult when blocked.
- Identify tempting advanced material that should be postponed.

### `02_学习环境与工具.md`

Interpret "environment" according to the domain.

- Programming: operating system, compiler/runtime, editor, debugger, package/build tools, verification commands.
- Language/exam: official syllabus, dictionary, audio source, timer, answer sheets, recording method.
- Mathematics/theory: core text, notation reference, writing tools, graphing/CAS policy, problem source.
- Practical craft: physical/digital tools, workspace, safety equipment, version/file management.

Separate minimum requirements from optional upgrades. Never claim tools are installed unless verified.

### `03_学习计划与阶段验收.md`

Connect time to outcomes:

- weekly budget and suggested cadence;
- phase durations as ranges, not promises;
- minimum viable route for busy periods;
- acceptance checks and remediation when a check fails;
- adjustment rules after illness, exams, work, or unexpected difficulty.

### `AGENTS.md`

The tutor specification that governs every future AI teaching session in this folder. Derive it from `assets/agents-md-template.md` and adapt it to the learner, domain, and machine; see the tutor specification section in `SKILL.md` for the required content. It is an authored document like the root guides: no unresolved placeholders, and no environment facts that were not actually established.

## `references/`

Put detailed authored learning guidance here. A useful reference document normally contains:

1. purpose and prerequisites;
2. mental model or concept map;
3. essential concepts;
4. guided examples where appropriate;
5. learner-owned practice specifications;
6. validation method or rubric;
7. common errors and diagnosis;
8. exit criteria;
9. sources when current or externally verified facts are used.

Numbering ranges organize files but do not impose quotas:

```text
00-09  orientation and prerequisites
10-19  core beginner material
20-29  intermediate capability
30-39  advanced practice or real-world work
40-49  optional tracks
50-79  official references and lookup guides
80-89  portfolio, review, and long-term development
```

Use `40-49` only for genuinely optional branches. Do not hide required prerequisites there.

## `books/`

Default to one reading-order file. List lawful access routes and explain when each long resource becomes useful. Do not create a large reading backlog or redistribute copyrighted files.

For each item record:

- title and author/organization;
- role in the route;
- relevant chapters or sections;
- prerequisites;
- access source if lawful and verified;
- whether it is required, optional, or lookup-only.

## `tools/`

Create only when the domain benefits from reusable, non-answer artifacts, such as:

- environment verification scripts;
- blank data-recording templates outside learner directories;
- rubric or checklist files;
- deterministic converters or validators;
- configuration templates with safe placeholders.

Do not put completed practice, starter solutions, opaque executables, downloaded installers, or generated build artifacts here. Prefer source and instructions.

## `notes/`, `projects/`, and `journal/`

Create all three directories and leave them completely empty.

- Practice descriptions belong in `references/`.
- Review instructions belong in `references/82_周复盘说明.md`.
- `projects/` receives everything the learner creates: code, experiments, results.
- `notes/` receives the learner's long-term review material, written by the AI tutor per `AGENTS.md` — one file per study block, not a chat log.
- `journal/` receives the tutor's teaching progress log and later review summaries.
- Do not add README files, templates, `.gitkeep`, hidden files, or sample content.

If a package will be stored in Git, explain outside these directories that Git does not track empty directories.

## Optional directories

Add a directory only when it has real content and the user needs it:

- `sources/`: small, redistributable source documents with clear licensing.
- `datasets/`: only small lawful data, with provenance and license.
- `media/`: user-provided or redistributable images/audio.
- `apps/`: only when an application was explicitly requested and can be maintained.

Avoid mirrored websites, giant PDFs, installers, archives, and duplicate rendered formats by default.

## Cross-file consistency

- Use relative links.
- Use one phase vocabulary throughout.
- Keep file names stable after linking them.
- Put each fact in one canonical place; summarize and link elsewhere.
- Ensure every listed file exists.
- Ensure the roadmap, use order, and acceptance plan describe the same progression.
