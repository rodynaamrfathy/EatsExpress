#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pycodestyle
import unittest
from console import YourCommand
from unittest.mock import patch
from io import StringIO

class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                        "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_YourCommand_class_docstring(self):
        """Test for the YourCommand class docstring"""
        self.assertIsNot(YourCommand.__doc__, None,
                        "YourCommand class needs a docstring")
        self.assertTrue(len(YourCommand.__doc__) >= 1,
                        "YourCommand class needs a docstring")

class TestYourCommand(unittest.TestCase):
    """Class for testing the functionality of YourCommand"""

    def setUp(self):
        """Set up for the tests"""
        self.cmd = YourCommand()

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("show InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("destroy InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

if __name__ == '__main__':
    unittest.main()
