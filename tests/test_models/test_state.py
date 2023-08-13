#!/usr/bin/python3
"""
    Test State module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
        Test State class
    """

    def test_should_create_state_instance(self):
        """
            Test State
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_should_create_state_variable(self):
        """
            Test Vars
        """
        state = State()
        self.assertIsInstance(state.name, str)
