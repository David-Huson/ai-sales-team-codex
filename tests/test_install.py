import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT/'scripts/manage_install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_install_repeat_resources_and_uninstall(self):
        with tempfile.TemporaryDirectory(prefix='sales skills ') as tmp:
            dest = Path(tmp)/'skills'
            self.assertEqual(installer.manage('install', dest), 14)
            self.assertEqual(installer.manage('install', dest), 14)
            for name in installer.NAMES:
                entry = dest/name/'SKILL.md'
                self.assertTrue(entry.is_file())
                self.assertTrue(entry.read_text().startswith(f'---\nname: {name}\n'))
                self.assertTrue((dest/name/'references/workflow.md').is_file())
            self.assertTrue((dest/'sales/scripts/generate_pdf_report.py').is_file())
            self.assertTrue((dest/'sales/templates/outreach-cold.md').is_file())
            (dest/'unrelated').mkdir()
            self.assertEqual(installer.manage('uninstall', dest), 14)
            self.assertTrue((dest/'unrelated').is_dir())
            self.assertEqual(installer.manage('uninstall', dest), 0)

    def test_conflict_does_not_partially_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            (dest/'sales-report-pdf').mkdir()
            with self.assertRaises(ValueError):
                installer.manage('install', dest)
            self.assertEqual(list(dest.iterdir()), [dest/'sales-report-pdf'])

    def test_foreign_and_broken_links_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            link = dest/'sales'
            link.symlink_to(dest/'missing')
            with self.assertRaises(ValueError):
                installer.manage('install', dest)
            self.assertEqual(installer.manage('uninstall', dest), 0)
            self.assertTrue(link.is_symlink())

    def test_checkout_discovery(self):
        entries = list((ROOT/'.agents/skills').iterdir())
        self.assertEqual(len(entries), 14)
        for entry in entries:
            self.assertTrue((entry/'SKILL.md').is_file())
            self.assertEqual(entry.resolve(), ROOT/'skills'/entry.name)


if __name__ == '__main__':
    unittest.main()
