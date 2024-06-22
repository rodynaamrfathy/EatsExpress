
#!/usr/bin/python3
"""
Contains the TestRestaurantDocs classes
"""

from datetime import datetime
import inspect
import models
from models import Restaurant
from models.base_model import BaseModel
import pep8
import unittest
Restaurant = restaurant.Restaurant

class TestRestaurantDocs(unittest.TestCase):
    """Tests to check the documentation and style of Restaurant class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.restaurant_f = inspect.getmembers(Restaurant, inspect.isfunction)

    def test_pep8_conformance_restaurant(self):
        """Test that models/restaurant.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/Restaurant.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_restaurant_module_docstring(self):
        """Test for the restaurant.py module docstring"""
        self.assertIsNot(restaurant.__doc__, None,
                        "restaurant.py needs a docstring")
        self.assertTrue(len(restaurant.__doc__) >= 1,
                        "restaurant.py needs a docstring")

    def test_restaurant_class_docstring(self):
        """Test for the Restaurant class docstring"""
        self.assertIsNot(Restaurant.__doc__, None,
                        "Restaurant class needs a docstring")
        self.assertTrue(len(Restaurant.__doc__) >= 1,
                        "Restaurant class needs a docstring")

    def test_restaurant_func_docstrings(self):
        """Test for the presence of docstrings in Restaurant methods"""
        for func in self.restaurant_f:
            self.assertIsNot(func[1].__doc__, None,
                            "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestRestaurant(unittest.TestCase):
    """Test the Restaurant class"""
    def test_is_subclass(self):
        """Test that Restaurant is a subclass of BaseModel"""
        restaurant = Restaurant()
        self.assertIsInstance(restaurant, BaseModel)
        self.assertTrue(hasattr(restaurant, "id"))
        self.assertTrue(hasattr(restaurant, "created_at"))
        self.assertTrue(hasattr(restaurant, "updated_at"))

    def test_attributes(self):
        """Test that Restaurant has specific attributes, and they are initialized correctly"""
        restaurant = Restaurant()
        # Assuming the Restaurant class has attributes such as name, location
        self.assertTrue(hasattr(restaurant, "name"))
        self.assertTrue(hasattr(restaurant, "location"))
        self.assertEqual(restaurant.name, "")
        self.assertEqual(restaurant.location, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Restaurant()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_str(self):
        """test that the str method has the correct output"""
        restaurant = Restaurant(name="Pizza Place", location="Main Street")
        string = "[Restaurant] ({}) {{}}".format(restaurant.id, restaurant.__dict__)
        self.assertIn("Pizza Place", string)
        self.assertIn("Main Street", string)

if __name__ == '__main__':
    unittest.main()
