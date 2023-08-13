#!/usr/bin/python3
"""
    TestBaseModel module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Tests base model class
    """

    def test_instance_creation_of_base_model(self):
        """
            Tests instance creation of the base model
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_avoid_id_duplication_for_instance(self):
        """
            Tests avoid ID duplications
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_assignment_of_created_at_attribute(self):
        """"
            Tests created_at attribute
        """
        bm = BaseModel()
        c_at = bm.created_at
        self.assertIsInstance(c_at, datetime)

    def test_date_format_for_created_at(self):
        """
            Tests date format for datetime attribute
        """
        bm = BaseModel()
        c_at = bm.created_at.__str__()
        c_at_pattern = '\d{4}\-\d{2}\-\d{2}\ \d{2}\:\d{2}\:\d{2}\.\d{6}'
        self.assertRegex(c_at, c_at_pattern)

    def test_assignment_of_updated_at_attribute(self):
        """
            Tests updated_at attribute
        """
        bm = BaseModel()
        u_at = bm.updated_at
        self.assertIsInstance(u_at, datetime)

    def test_date_format_for_updated_at(self):
        """
            Tests date format for datetime attribute
        """
        bm = BaseModel()
        u_at = bm.updated_at.__str__()
        u_at_pattern = '\d{4}\-\d{2}\-\d{2}\ \d{2}\:\d{2}\:\d{2}\.\d{6}'
        self.assertRegex(u_at, u_at_pattern)

    def test_str_magic_function_with_empty_attributes(self):
        """
            Tests humain readable format
        """
        bm = BaseModel()
        s = bm.__str__()
        frmt = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(s, frmt)

    def test_str_magic_function_with_non_empty_attributes(self):
        """
            Tests humain readable format
        """
        bm = BaseModel()
        bm.name = "Betty"
        bm.year = 1917
        s = bm.__str__()
        frmt = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(s, frmt)

    def test_save_method_behavior_for_updating_attributres(self):
        """
            Tests Updated_at
        """
        bm = BaseModel()
        update_in_create = bm.updated_at
        bm.save()
        update_in_save = bm.updated_at
        self.assertNotEqual(update_in_create, update_in_save)

    def test_to_dict_behavior_for_dict_format_return(self):
        """
            Tests to_dict method
        """
        bm = BaseModel()
        bm.name = "Holberton"
        bm.number = 89
        bm_model = bm.to_dict()
        c_at = bm.created_at.isoformat()
        u_at = bm.updated_at.isoformat()
        bm_id = bm.id
        expected = {
            "name": "Holberton",
            "number": 89,
            "id": bm_id,
            "__class__": "BaseModel",
            "created_at": c_at,
            "updated_at": u_at
        }
        self.assertDictEqual(bm_model, expected)

    def test_to_dict_created_instance(self):
        """
            Tests attribute instance and type
        """
        bm = BaseModel()
        bm.name = "Betty"
        bm.number = 89
        bm_json = bm.to_dict()
        self.assertIsInstance(bm_json["number"], int)
        self.assertIsInstance(bm_json["name"], str)
        self.assertIsInstance(bm_json["__class__"], str)
        self.assertIsInstance(bm_json["updated_at"], str)
        self.assertIsInstance(bm_json["created_at"], str)
        self.assertIsInstance(bm_json["id"], str)

    def test_str(self):
        """
            Test __str__ method
        """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_instance_creation_with_kwargs_single_argument(self):
        """
            Test instance creation with kwargs
        """
        kwargs = {"name": "Betty"}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.name, "Betty")

    def test_instance_creation_with_kwargs_multi_args(self):
        """
            Test instance
        """
        kwargs = {"name": "Betty", "number": 89}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.name, "Betty")
        self.assertEqual(bm.number, 89)

    def test_instance_creation_with_id(self):
        """
            Test predefined id
        """
        b_id = 'c1586632-9ab1-4894-a5d9-fe55c1571ef1'
        kwargs = {"id": b_id}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, b_id)

    def test_instance_creation_with_created_at_as_datetime(self):
        """
            Tests created at
        """
        c_at = '2017-09-28T21:03:54.052302'
        kwargs = {"created_at": c_at}
        bm = BaseModel(**kwargs)
        self.assertIsInstance(bm.created_at, datetime)

    def test_instance_creation_with_updated_at_as_datetime(self):
        """
            Tests updated at
        """
        u_at = '2017-09-28T21:03:54.052302'
        kwargs = {"updated_at": u_at}
        bm = BaseModel(**kwargs)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_instance_creation_with_created_at_attr(self):
        """
            Tests created at
        """
        c_at = '2017-09-28T21:03:54.052302'
        kwargs = {"created_at": c_at}
        bm = BaseModel(**kwargs)
        c_expected = datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(bm.created_at, c_expected)

    def test_instance_creation_with_created_at_attr(self):
        """
            Tests updated at
        """
        u_at = '2017-09-28T21:03:54.052302'
        kwargs = {"updated_at": u_at}
        bm = BaseModel(**kwargs)
        u_expected = datetime(2017, 9, 28, 21, 3, 54, 52302)
        self.assertEqual(bm.updated_at, u_expected)

    def test_should_not_add__class__to_the_attributes(self):
        """
            Tests should not add __class__ to the attribute
        """
        kwargs = {"__class__": "FakeBaseModel"}
        bm = BaseModel(**kwargs)
        self.assertNotEqual(bm.__class__, "FakeBaseModel")

    def test_should_add__class__to_the_attributes(self):
        """
            Tests should not add __class__ to the attribute
        """
        kwargs = {"__class__": "FakeBaseModel"}
        bm = BaseModel(**kwargs)
        self.assertEqual(str(bm.__class__),
                         "<class 'models.base_model.BaseModel'>")

    def test_id_type(self):
        """[test type of id]
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
