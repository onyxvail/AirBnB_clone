#!/usr/bin/python3
"""
    Test City module
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
        Test City class
    """

    def test_should_create_intance_of_city(self):
        """
            Test the creation of instance
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_should_create_instance_variable(self):
        """
            Test var
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
