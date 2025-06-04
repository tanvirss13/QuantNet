import pathlib
import unittest

class TestReadme(unittest.TestCase):
    def test_cppforfinancial_readme_has_compiler(self):
        path = pathlib.Path('CppForFinancialEngg/README.md')
        content = path.read_text(encoding='utf-8')
        self.assertIn('Compiler and Linker Errors', content)
        self.assertNotIn('Comipler', content)

if __name__ == '__main__':
    unittest.main()
