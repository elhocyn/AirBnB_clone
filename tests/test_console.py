import unittest
from unittest.mock import patch
from io import StringIO
import console
import pycodestyle


class TestConsole(unittest.TestCase):
    def test_module_docstring(self):
        """Test that the module has a docstring"""
        self.assertIsNotNone(console.__doc__)

    def test_class_docstring(self):
        """Test that the class has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.__doc__)

    def test_quit_docstring(self):
        """Test that the quit method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.do_quit.__doc__)

    def test_EOF_docstring(self):
        """Test that the EOF method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.do_EOF.__doc__)

    def test_emptyline_docstring(self):
        """Test that the emptyline method has a docstring"""
        self.assertIsNotNone(console.HBNBCommand.emptyline.__doc__)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('quit')
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('EOF')
            output = f.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command(self):
        """Test the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
