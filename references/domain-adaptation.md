# Domain Adaptation

Choose the learning loop that matches the subject. The directory architecture is shared; the pedagogy is not.

## Programming and engineering

Typical progression:

```text
environment and syntax
-> data and program structure
-> debugging and testing
-> engineering tools
-> performance/concurrency where relevant
-> independent projects
```

Required characteristics:

- verify the toolchain before ambitious exercises;
- teach correctness and diagnosis before optimization;
- distinguish language learning from framework accumulation;
- include small executable tasks and tests;
- introduce version control as evidence/history, not a commit-count game;
- keep platform-specific instructions explicit;
- place project briefs in `references/`, leaving `projects/` empty.

For HPC, add a measurement-first progression: single-core behavior before shared-memory parallelism, then distributed/GPU work, then cluster/competition engineering. Hardware counters and GPU tools must be qualified by environment.

## Language learning and standardized exams

Typical progression:

```text
diagnostic assessment
-> foundational gaps
-> component skills
-> integrated timed practice
-> full simulations
-> targeted remediation
```

Required characteristics:

- anchor exam content to the current official syllabus when available;
- distinguish language ability from test strategy;
- distribute vocabulary and grammar through listening/reading/writing contexts;
- specify legal practice sources instead of redistributing copyrighted papers;
- include timing, scoring rubric, and an error taxonomy;
- use periodic diagnostics to change the plan;
- do not promise a score from study hours.

For `tools/`, useful items might be a blank writing rubric or timing checklist. Do not create filled answer sheets or a learner's error log; those belong to the learner.

## Mathematics and theoretical subjects

Typical progression:

```text
prerequisite diagnosis
-> definitions and representations
-> core techniques
-> mixed problems and proofs
-> applications
-> cumulative synthesis
```

Required characteristics:

- map prerequisite dependencies explicitly;
- balance intuition, formal definitions, and problem solving;
- use worked examples to model reasoning, then require independent transfer;
- include retrieval and cumulative review, not only chapter-end practice;
- specify when calculators, CAS, or coding are allowed;
- validate explanations, not only final answers.

## Natural and social sciences

Typical progression:

```text
foundational concepts
-> models and evidence
-> methods/data interpretation
-> domain applications
-> synthesis and critique
```

Required characteristics:

- distinguish models from observed reality;
- teach units, assumptions, uncertainty, and evidence quality;
- include graph/data interpretation;
- add laboratory or field safety where relevant;
- separate consensus knowledge from contested or changing claims.

## Practical and creative skills

Typical progression:

```text
tools and safety
-> constrained drills
-> imitation/analysis
-> independent artifacts
-> critique and iteration
-> portfolio
```

Required characteristics:

- define quality with rubrics and examples, not taste alone;
- include feedback sources and revision cycles;
- avoid prescribing one aesthetic as universal;
- identify material cost, equipment, and accessibility needs;
- keep learner artifacts out of the generated package.

## Career and professional skills

Typical progression:

```text
role/task model
-> foundational techniques
-> realistic scenarios
-> reviewed deliverables
-> portfolio and interview transfer
```

Required characteristics:

- use realistic deliverables and constraints;
- distinguish current industry practice from durable principles;
- protect confidential and personal data;
- avoid unsupported job-market and salary claims;
- validate recommendations against the target region/role when current research is possible.

## Mixed and interdisciplinary subjects

Create one required spine and optional branches. For example:

```text
programming + statistics spine
-> shared tooling and reproducibility
-> optional genomics / finance / robotics track
```

Avoid requiring domain depth before the learner can run a first meaningful experiment, but do not skip safety or conceptual prerequisites that protect correctness.

## Adaptation questions

Before finalizing, ask internally:

1. What does competent performance look like in this field?
2. What feedback can the learner obtain without an expert present?
3. Which prerequisites cause most failures?
4. Which facts are time-sensitive?
5. What work must remain learner-owned?
6. What safety, legal, or ethical boundaries apply?
