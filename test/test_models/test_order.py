
import unittest
from models.order import Order

class TestOrder(unittest.TestCase):
    """Unit tests for the Order class"""

    def test_instance_creation(self):
        """Test creation of Order instance"""
        instance = Order()
        self.assertIsInstance(instance, Order)

    def test_attributes(self):
        """Test default attributes of Order"""
        instance = Order()
        self.assertTrue(hasattr(instance, 'order_id'))
        self.assertTrue(hasattr(instance, 'status'))

if __name__ == '__main__':
    unittest.main()
