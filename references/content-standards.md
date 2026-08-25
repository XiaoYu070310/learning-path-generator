# Content Standards

## Write for action

Every substantial section should help the learner decide, do, observe, or correct something. Prefer:

```text
Concept -> small practice -> evidence -> explanation -> next step
```

Avoid long catalogs without instructions for use.

## Separate learning materials from learner work

The package may define a task but must not perform it on behalf of the learner.

A good task specification includes:

- purpose;
- prerequisites;
- input or starting conditions;
- constraints;
- expected learner-created artifact;
- correctness or quality checks;
- reflection questions;
- optional extension.

It should not include the final answer, completed project, fabricated measurements, filled review, or a solution disguised as starter material.

Worked examples are allowed when they teach a concept, but the assessed task should require independent transfer rather than copying.

## Acceptance criteria

Use observable evidence appropriate to the domain:

- Programming: program output, tests, build reproducibility, debugging evidence, explanation of tradeoffs.
- Language: timed accuracy, comprehension evidence, recordings, rubric-scored writing, error-category reduction.
- Mathematics: correct solutions, proof explanations, transfer problems, cumulative retention checks.
- Practical skill: deliverable quality, process safety, critique against a rubric, reproducibility.
- Research: question formulation, source quality, transparent method, uncertainty, reproducible analysis.

Avoid "watched the course", "studied for 20 hours", or "made 10 commits" as primary proof.

## Sources and freshness

For current facts, include a source note:

```markdown
## Sources

- [Official title](https://example.org/path) - used for the current syllabus; accessed YYYY-MM-DD.
```

- Prefer official documentation for specifications, exams, software, competitions, and policies.
- Use stable deep links rather than a generic home page when possible.
- Never invent links or imply verification that did not happen.
- Date information that can change.
- Explain uncertainty and tell the learner what to confirm.

Do not cite sources merely to decorate stable explanations.

## Commands and code

- State the platform and shell.
- Use the learner's declared environment.
- Keep paths relative or use clear placeholders such as `<package-path>`.
- Explain destructive commands and safer alternatives.
- Provide verification output patterns, not fabricated claims that a command succeeded.
- Keep debugging and performance builds distinct.
- Mark version-sensitive options.

For commands copied from external documentation, verify current syntax when internet access is available.

## Estimates and claims

- Give time estimates as ranges and name their assumptions.
- Do not promise a score, job, admission, competition result, fluency level, or speedup.
- Treat benchmark numbers as hardware/workload-specific.
- Distinguish "commonly useful" from "always best".
- Do not assign arbitrary universal thresholds without a source or domain rationale.

## Safety, legality, and ethics

Add relevant cautions for:

- destructive system commands and privileged installation;
- physical activities, laboratory work, health, or electrical tools;
- personal data and credentials;
- copyrighted books, leaked exams, proprietary datasets, and paid courses;
- academic integrity and use of solutions;
- consequential professional advice.

## Style

- Match the user's language and level.
- Define specialized terminology on first use.
- Use short headings and tables where comparison helps.
- Avoid repeated conclusions across files.
- Avoid inflated language, generic encouragement, and excessive rhetorical framing.
- Keep filenames descriptive and sortable.
- Prefer ASCII in code and paths unless the platform and context clearly support Unicode.

## Quality over volume

Do not maximize file count. A smaller coherent package is better than dozens of shallow files. Split a document when it has a distinct use time, audience, or task; otherwise keep related content together.
