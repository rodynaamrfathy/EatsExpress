
import unittest
from models.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    """Unit tests for the Restaurant class"""

    def test_instance_creation(self):
        """Test creation of Restaurant instance"""
        instance = Restaurant()
        self.assertIsInstance(instance, Restaurant)

    def test_attributes(self):
        """Test default attributes of Restaurant"""
        instance = Restaurant()
        self.assertTrue(hasattr(instance, 'name'))
        self.assertTrue(hasattr(instance, 'location'))

if __name__ == '__main__':
    unittest.main()
