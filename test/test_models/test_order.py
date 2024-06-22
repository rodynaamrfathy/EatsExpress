#!/usr/bin/python3
"""
Contains the TestOrderDocs classes
"""

from datetime import datetime
import inspect
import models
from models.order import Order
from models.base_model import BaseModel
import pep8
import unittest


class TestOrderDocs(unittest.TestCase):
    """Tests to check the documentation and style of Order class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.order_f = inspect.getmembers(Order, inspect.isfunction)

    def test_pep8_conformance_order(self):
        """Test that models/order.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/order.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_order_module_docstring(self):
        """Test for the order.py module docstring"""
        self.assertIsNot(models.order.__doc__, None,
                        "order.py needs a docstring")
        self.assertTrue(len(models.order.__doc__) >= 1,
                        "order.py needs a docstring")

    def test_order_class_docstring(self):
        """Test for the Order class docstring"""
        self.assertIsNot(Order.__doc__, None,
                        "Order class needs a docstring")
        self.assertTrue(len(Order.__doc__) >= 1,
                        "Order class needs a docstring")

    def test_order_func_docstrings(self):
        """Test for the presence of docstrings in Order methods"""
        for func in self.order_f:
            self.assertIsNot(func[1].__doc__, None,
                            "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOrder(unittest.TestCase):
    """Test the Order class"""
    def test_is_subclass(self):
        """Test that Order is a subclass of BaseModel"""
        order = Order()
        self.assertIsInstance(order, BaseModel)
        self.assertTrue(hasattr(order, "id"))
        self.assertTrue(hasattr(order, "created_at"))
        self.assertTrue(hasattr(order, "updated_at"))

    def test_attributes(self):
        """Test that Order has necessary attributes"""
        order = Order()
        self.assertTrue(hasattr(order, "user_id"))
        self.assertTrue(hasattr(order, "product_name"))
        self.assertTrue(hasattr(order, "quantity"))
        self.assertTrue(hasattr(order, "price"))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        order = Order()
        new_d = order.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in order.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_str(self):
        """test that the str method has the correct output"""
        order = Order()
        string = "[Order] ({}) {}".format(order.id, order.__dict__)
        self.assertEqual(string, str(order))
