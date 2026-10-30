<div align="center">

![Storytelling Conversion: clear, credible marketing stories](assets/banner.svg)

# Storytelling Conversion

**Eight storytelling principles for purposeful business communication.**

Build attention, establish the world of a problem, make ideas imaginable, and deliver an earned resolution. Apply the method to emails, posts, pages, scripts, edits, and content strategy.

[![Validate](https://github.com/takimdigital/storytelling-conversion/actions/workflows/validate.yml/badge.svg)](https://github.com/takimdigital/storytelling-conversion/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/takimdigital/storytelling-conversion)](https://github.com/takimdigital/storytelling-conversion/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-2563eb.svg)](LICENSE)

[Install](#install) · [Try it](#try-it) · [Examples](examples/README.md) · [Contribute](CONTRIBUTING.md)

</div>

## What it does

Storytelling Conversion gives an AI assistant a connected narrative method: predictive processing, establishing shots, word pictures, story structure, Chekhov's gun, a specific villain, sugar coating, and bookending. Each principle includes a procedure and an inspection, not just a reminder to write engaging copy.

It first identifies the work needed. The result can be a direct answer, a focused edit, a new piece, or a narrative marketing direction. It can recommend repairing an existing message instead of producing another asset.

Use it to:

- Improve an opening that feels vague or loses attention.
- Explain a product through a recognizable situation and a clear mechanism.
- Write emails, landing-page sections, social posts, sales scripts, and case studies.
- Diagnose a story that sounds polished but never makes its point.
- Adapt a narrative for another format or language.
- Make a precise edit while preserving the rest of the copy.
- Discover whether an existing answer is buried, unclear, or missing.
- Choose a small communication experiment within a realistic time budget.

The skill keeps customer stories, illustrations, and measured results distinct. It gives unsupported claims a useful alternative and an evidence requirement. Short utility copy stays short.

## What the method changes

**Fictional brief:** A document-review tool shows unresolved comments beside their relevant passages. Write an email for project leads preparing a draft for approval.

An ordinary summary lists that feature. A narrative approach opens a relevant uncertainty:

> **Subject: The yellow mark on the last page**
>
> Imagine the proposal is ready to send. The paragraphs are polished. Then you reach a yellow comment on the final page: which delivery date are we promising?
>
> The writing is finished. The decision is still open.

The body can teach a useful final-review method, introduce the tool at the relevant mechanism, and return to that mark with a changed meaning of finished. The complete [worked example](skills/storytelling-conversion/references/production.md) explains the design and payoff. This is an authored illustration, not a customer account or measured result.

## Install

### Codex: ask the skill installer

Paste this into Codex:

```text
$skill-installer install https://github.com/takimdigital/storytelling-conversion/tree/main/skills/storytelling-conversion
```

For a version-pinned installation, replace `main` with `v1.2.1`. If an existing installation conflicts, review it before replacing it. If the skill does not appear, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

### Manual installation

Download a [release](https://github.com/takimdigital/storytelling-conversion/releases/latest) or clone this repository, then copy the **entire** `skills/storytelling-conversion` folder into your agent's skills directory. Include its `references` and `agents` folders.

For Codex, use `.agents/skills/` in your project, or `~/.agents/skills/` for your user account. The resulting path should end with `storytelling-conversion/SKILL.md`.

The `.skill` release asset is a ZIP archive containing that folder. Extract it with a ZIP-compatible tool; it is not an executable installer. Each release includes a SHA-256 checksum.

### Other assistants

The core instructions use the [Agent Skills format](https://agentskills.io/specification). Assistants that support this format may use the skill, but their discovery paths and invocation syntax vary. Codex is the documented installation target; other integrations have not been independently verified. You can also supply the Markdown instructions and relevant references directly to your assistant.

## Try it

```text
Use $storytelling-conversion to rewrite this landing-page section.

Audience: freelance designers.
Verified product facts: clients can choose an available appointment time
and receive an email confirmation.
Goal: invite the reader to try booking.
Voice: practical and friendly.
Limit: 80 words. Do not invent customer outcomes.

Draft: [paste your copy]
```

For a targeted edit:

```text
Use $storytelling-conversion to improve only the first sentence.
Keep the offer, facts, and remaining copy unchanged.
[paste your copy]
```

For an audit:

```text
Use $storytelling-conversion to find the three most important problems
in this sales story. Explain each problem and give a concrete repair.
Separate unsupported claims from writing issues.
[paste your story and supporting facts]
```

More prompts and illustrative outputs: [examples](examples/README.md).

## How it works

1. **Establish the assignment.** Identify the audience, awareness, offer, action, emotional starting point, and scope.
2. **Design the obstacle and experience.** Develop the consequences, sustaining forces, attempted fixes, medicine, sugar, and desired emotional movement.
3. **Map the narrative.** Choose a structure and its beats; connect the opening uncertainty, word picture, important setups, and closing return.
4. **Write the requested work.** Make the product mechanism relevant to the story's actual problem.
5. **Edit through the method.** Inspect opening orientation, imagery, line jobs, open loops, and the ending's changed meaning.
6. **Preserve truth and scope.** Keep facts, conditions, fictional framing, voice, and permissions intact.

| Principle | Practical procedure |
|---|---|
| Predictive processing | Audience expectation, relevant uncertainty, sensory anchor, earned turn |
| Establishing shot | Where, who, mood, focus; opening-only inspection |
| Word pictures | Replace abstractions; purposeful sensory detail; mental-image exercise |
| Structure | Select Save the Cat, PAS, Hero's Journey, or ABT for the intended experience |
| Chekhov's gun | Setup/payoff ledger and line-job edit |
| Villain | Consequences, external forces, attempted fixes, failure mechanism |
| Sugar coating | Medicine, sugar, carrier, recoverable lesson |
| Bookending | Emotional endpoints, planted element, changed meaning, removal inspection |

Substantive writing considers all eight. A simple factual answer or narrow correction stays proportional to its request.

## What's included

```text
skills/storytelling-conversion/
├── SKILL.md                 Core workflow and trigger description
├── LICENSE                  License travels with the installed skill
├── agents/openai.yaml       Codex display metadata
└── references/
    ├── principles.md        Narrative choices and practical tests
    ├── direction.md         Discovery and small marketing decisions
    ├── production.md        Briefs, evidence, formats, and experiments
    └── review.md            Review rubric, examples, and repairs
```

The installed skill is instruction-only. It requires no API key, account connection, executable helper, or external service. This repository's Python scripts are maintenance tools, not part of the installed skill.

## Quality and limitations

Repository automation checks structure, local links, scenario fixtures, and reproducible packaging. Version 1.2.0 was manually audited for completeness of the method; no new writing or agent comparison was performed for it. Earlier exploratory comparisons concerned earlier revisions and do not validate this rewrite. See [evaluation guidance](evals/README.md). The skill makes no guarantee about attention, memory, conversion, or missing customer evidence.

Drafting copy does not authorize publication, scheduling, account access, spending, or deployment. Follow the permissions and project rules in your own environment.

## Maintain and contribute

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build.py
```

Python 3.11+ is required for repository tooling. There are no third-party Python dependencies.

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the edit, review, and release process. Report a reproducible problem through [GitHub Issues](https://github.com/takimdigital/storytelling-conversion/issues/new/choose). Include a sanitized prompt, the result, and the behavior you expected.

**License:** [MIT](LICENSE). You may use, adapt, and redistribute the skill under its terms.
