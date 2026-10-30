# Contributing

Improve a demonstrated writing or maintenance problem with the smallest useful change. Keep the installed skill portable, instruction-only, and independent of any particular business.

## Propose a change

Open an issue with a sanitized prompt, actual behavior, expected behavior, and relevant version. For a writing problem, include the verified facts and requested scope. Remove customer identities, account data, and private material.

For a pull request:

1. Edit `skills/storytelling-conversion/`. It is the canonical installable source.
2. Update examples or add a case to `evals/cases.json` when the behavior changes.
3. Run the checks below and review the diff.
4. Explain what improved, what you checked, and any remaining limitations.

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build.py
```

Use Python 3.11 or later. No dependency installation is required.

## Writing review

Run the relevant case prompts with the revised skill. Check factual support, edit boundaries, useful alternatives, and clarity. Record the assistant/model and date if you share results. Label human judgments and measured behavior separately. Avoid optimizing the skill solely to repeat the worked examples.

CI checks the files and build mechanics. It does not run an AI model, grade writing quality, or measure conversion performance.

## Release process for maintainers

1. Merge reviewed changes after CI passes.
2. Update `VERSION` and `CHANGELOG.md` together. Use a new version for changed release contents.
3. Run validation, tests, and a local build.
4. Push a tag matching `VERSION`, for example `v1.0.1`.
5. The release workflow verifies the tag, builds the package and checksum, and creates the GitHub release.
6. Check the release assets and try a version-pinned install into an isolated skills folder.

Never move a published version tag to different content. Document installation or invocation changes prominently. Use a major version for incompatible changes, a minor version for compatible capabilities, and a patch version for corrections.

The repository is the source of truth. Local installed copies should be updated deliberately, after preserving personal changes.
