# Repository maintenance

The canonical skill is `skills/storytelling-conversion/`. Keep runtime instructions there; keep project maintenance instructions and documentation outside the installable folder.

Preserve factual safeguards, narrow-edit behavior, language support, and the distinction between editorial review and measured audience results. Do not add product-specific paths, private examples, analytics exports, or account information.

Before changing release content, inspect `VERSION`, `CHANGELOG.md`, and `evals/cases.json`. For substantive instruction changes, exercise relevant scenarios and record limitations. Follow `CONTRIBUTING.md` for releases; do not publish or retag without the repository owner's authorization.

Run `python scripts/validate.py`, `python -m unittest discover -s tests -v`, and `python scripts/build.py` before completing changes. Do not commit `dist/`, caches, or local test outputs.
