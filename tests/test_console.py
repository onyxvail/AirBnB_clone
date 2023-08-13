#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """
        TestConsole class
    """
    def test_help_console_cmd(self):
        """
        Test <help>
        """
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_help_quit_console_cmd(self):
        """
        Tests <help quit>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertRegex(f.getvalue(), '^Quit command')

    def test_help_EOF_console_cmd(self):
        """
        Tests <help EOF>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertRegex(f.getvalue(), '^EOF command')

    def test_help_create_console_cmd(self):
        """
        Tests <help create>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertRegex(f.getvalue(), '^Create command')

    def test_create_console_cmd_should_fail_without_clsname(self):
        """
        Test <create>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_create_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <create WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_create_console_cmd_should_work_properly(self):
        """
        Test <create BaseModel>
        """
        instance_before = len(storage.all())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            instance_after = len(storage.all())
            self.assertEqual(instance_before + 1, instance_after)

    def test_help_show_console_cmd(self):
        """
        Tests <help show>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertRegex(f.getvalue(), '^Show command')

    def test_show_console_cmd_should_fails_without_clsname(self):
        """
        Tests <show>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <show WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_without_id(self):
        """
        Test <show BaseModel>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            expected = "** instance id missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_show_console_cmd_should_fail_with_wrong_id(self):
        """
        Test <show BaseModel 1212121212>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1212121212")
            expected = "** no instance found **\n"
            self.assertEqual(expected, f.getvalue())

    def test_help_destroy_console_cmd(self):
        """
        Tests <help destroy>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertRegex(f.getvalue(), '^Destroy command')

    def test_destroy_console_cmd_should_fails_without_clsname(self):
        """
        Tests <destroy>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected = "** class name missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <destroy WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_without_id(self):
        """
        Test <destroy BaseModel>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected = "** instance id missing **\n"
            self.assertEqual(expected, f.getvalue())

    def test_destroy_console_cmd_should_fail_with_wrong_id(self):
        """
        Test <destroy BaseModel 1212121212>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1212121212")
            expected = "** no instance found **\n"
            self.assertEqual(expected, f.getvalue())

    def test_help_all_console_cmd(self):
        """
        Tests <help all>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertRegex(f.getvalue(), '^All command')

    def test_all_console_cmd_should_fail_with_wrong_clsname(self):
        """
        Test <all WrongClsName>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all WrongClsName")
            expected = "** class doesn't exist **\n"
            self.assertEqual(expected, f.getvalue())

    def test_help_update_console_cmd(self):
        """
        Tests <help update>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertRegex(f.getvalue(), '^Update command')
