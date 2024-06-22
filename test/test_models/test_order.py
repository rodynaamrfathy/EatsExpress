
#!/usr/bin/python3
"""
Contains the TestOrderDocs classes
"""

from datetime import datetime
import inspect
import models
from models import Order
from models.base_model import BaseModel
import pep8
import unittest
Order = order.Order

class TestOrderDocs(unittest.TestCase):
    """Tests to check the documentation and style of Order class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.order_f = inspect.getmembers(Order, inspect.isfunction)

    def test_pep8_conformance_order(self):
        """Test that models/order.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/Order.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_order_module_docstring(self):
        """Test for the order.py module docstring"""
        self.assertIsNot(order.__doc__, None,
                         "order.py needs a docstring")
        self.assertTrue(len(order.__doc__) >= 1,
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
        """Test that Order has specific attributes, and they are initialized correctly"""
        order = Order()
        # Assuming the Order class has attributes such as order_id, item_name, quantity
        self.assertTrue(hasattr(order, "order_id"))
        self.assertTrue(hasattr(order, "item_name"))
        self.assertTrue(hasattr(order, "quantity"))
        self.assertEqual(order.item_name, "")
        self.assertEqual(order.quantity, 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        o = Order()
        new_d = o.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_str(self):
        """test that the str method has the correct output"""
        order = Order(item_name="Pizza", quantity=2)
        string = "[Order] ({}) {{}}".format(order.id, order.__dict__)
        self.assertIn("Pizza", string)
        self.assertIn("2", string)

if __name__ == '__main__':
    unittest.main()
