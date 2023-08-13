#!/usr/bin/python3
"""
    Test Amenity module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        Test Amenity class
    """

    def test_should_create_amenity_instance(self):
        """
            Test amenity
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_shoudl_create_instance_variables(self):
        """
            Test vars
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
