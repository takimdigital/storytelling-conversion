"""Build a reproducible .skill ZIP and checksum without external dependencies."""

from __future__ import annotations

import hashlib
from pathlib import Path
import zipfile

from validate import ROOT, SKILL, REQUIRED_SKILL_FILES, validate


def build(root: Path = ROOT, output: Path | None = None) -> Path:
    failures = validate(root)
    if failures:
        raise ValueError('\n'.join(failures))
    output = output or root / 'dist'
    output.mkdir(parents=True, exist_ok=True)
    archive = output / 'storytelling-conversion.skill'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_STORED) as package:
        for name in sorted(REQUIRED_SKILL_FILES):
            # Canonical line endings, timestamp, permissions, and order make
            # package hashes stable across checkout platforms and build dates.
            content = (root / SKILL / name).read_text(encoding='utf-8-sig')
            content = content.replace('\r\n', '\n').replace('\r', '\n')
            info = zipfile.ZipInfo(f'storytelling-conversion/{name}', (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            package.writestr(info, content.encode('utf-8'))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / 'SHA256SUMS').write_text(f'{digest}  {archive.name}\n', encoding='utf-8', newline='\n')
    return archive


if __name__ == '__main__':
    artifact = build()
    print(f'Built {artifact.name} and SHA256SUMS in {artifact.parent}')
