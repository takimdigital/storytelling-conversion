"""Test release boundaries and validation failures, without running an AI model."""

import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import build
from validate import REQUIRED_SKILL_FILES, SKILL, validate


class RepositoryTests(unittest.TestCase):
    def test_repository_validates(self):
        self.assertEqual(validate(), [])

    def test_reproducible_archive_and_checksum(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            first = build(output=directory / 'first')
            second = build(output=directory / 'second')
            self.assertEqual(first.read_bytes(), second.read_bytes())
            checksum = (first.parent / 'SHA256SUMS').read_text().split()[0]
            self.assertEqual(checksum, hashlib.sha256(first.read_bytes()).hexdigest())
            with zipfile.ZipFile(first) as package:
                self.assertIsNone(package.testzip())
                names = {f'storytelling-conversion/{name}' for name in REQUIRED_SKILL_FILES}
                self.assertEqual(set(package.namelist()), names)
                self.assertTrue(all(not name.startswith('/') and '..' not in Path(name).parts
                                    for name in package.namelist()))

    def test_missing_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / 'repository'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))
            reference = copy / SKILL / 'references/review.md'
            reference.unlink()
            failures = validate(copy)
            self.assertTrue(any('missing=' in error for error in failures))
            self.assertTrue(any('Broken/local-outside link' in error for error in failures))
            with self.assertRaises(ValueError):
                build(copy)

    def test_private_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / 'repository'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))
            (copy / 'private-note.md').write_text('C:' + '/Users/' + 'example/private', encoding='utf-8')
            self.assertTrue(any('Local user path' in error for error in validate(copy)))


if __name__ == '__main__':
    unittest.main()
