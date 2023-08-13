#!/usr/bin/python3
"""
    Test Place module
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
        Test Place class
    """

    def test_should_create_place_instance(self):
        """
            Tests place intance
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_should_create_the_right_type(self):
        """
            Tests the type of instance vars
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
