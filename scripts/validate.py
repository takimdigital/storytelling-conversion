"""Validate this repository's instruction-only skill and local documentation."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/storytelling-conversion')
REQUIRED_SKILL_FILES = {
    'SKILL.md', 'LICENSE', 'agents/openai.yaml', 'references/principles.md',
    'references/production.md', 'references/review.md',
}
IGNORED = {'.git', 'dist', '__pycache__', '.venv', 'local-results'}


def source_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(part in IGNORED for part in p.relative_to(root).parts))


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skill_dir = root / SKILL
    actual = {p.relative_to(skill_dir).as_posix() for p in skill_dir.rglob('*')
              if p.is_file()}
    if actual != REQUIRED_SKILL_FILES:
        errors.append(f'Skill files differ: missing={sorted(REQUIRED_SKILL_FILES - actual)}, '
                      f'unexpected={sorted(actual - REQUIRED_SKILL_FILES)}')

    version_path = root / 'VERSION'
    version = version_path.read_text(encoding='utf-8').strip() if version_path.exists() else ''
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        errors.append('VERSION must contain a semantic version such as 1.0.0')
    changelog = root / 'CHANGELOG.md'
    if not changelog.exists() or f'## {version} ' not in changelog.read_text(encoding='utf-8'):
        errors.append('CHANGELOG must include VERSION')

    entry = skill_dir / 'SKILL.md'
    if entry.exists():
        body = entry.read_text(encoding='utf-8-sig')
        front = re.match(r'\A---\n(.*?)\n---\n', body, re.S)
        if not front:
            errors.append('SKILL.md requires YAML frontmatter')
        else:
            fields = dict(re.findall(r'^(name|description): (.+)$', front.group(1), re.M))
            if fields.get('name') != skill_dir.name:
                errors.append('Skill name must match its folder')
            if not fields.get('description'):
                errors.append('Skill description is required')

    for path in source_files(root):
        if path.is_symlink():
            errors.append(f'Symlink not allowed: {path.relative_to(root)}')
            continue
        try:
            content = path.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            errors.append(f'Expected text source: {path.relative_to(root)}')
            continue
        if re.search(r'[A-Za-z]:[\\/]Users[\\/]', content):
            errors.append(f'Local user path in {path.relative_to(root)}')
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', content):
            errors.append(f'Private key in {path.relative_to(root)}')
        if path.suffix == '.md':
            # Check file targets, ignoring fenced examples and external links.
            prose = re.sub(r'```.*?```', '', content, flags=re.S)
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', prose):
                target = target.strip().strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve()
                if not destination.is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f'Broken/local-outside link in {path.relative_to(root)}: {target}')

    try:
        cases = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))
        ids: set[str] = set()
        if cases.get('skill_name') != 'storytelling-conversion' or not cases.get('cases'):
            errors.append('Evaluation cases must identify the skill and contain scenarios')
        for case in cases.get('cases', []):
            if not case.get('id') or case['id'] in ids or not case.get('prompt') or not case.get('checks'):
                errors.append('Evaluation cases need unique ids, prompts, and review checks')
            ids.add(case.get('id', ''))
    except (OSError, ValueError) as exc:
        errors.append(f'Cannot read evaluation cases: {exc}')
    return errors


if __name__ == '__main__':
    failures = validate()
    for failure in failures:
        print(f'ERROR: {failure}')
    if failures:
        raise SystemExit(1)
    print('Valid: skill structure, local links, release metadata, and scenario fixtures.')
