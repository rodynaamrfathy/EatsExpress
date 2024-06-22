
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unit tests for the Review class"""

    def test_instance_creation(self):
        """Test creation of Review instance"""
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_attributes(self):
        """Test default attributes of Review"""
        instance = Review()
        self.assertTrue(hasattr(instance, 'review_id'))
        self.assertTrue(hasattr(instance, 'content'))

if __name__ == '__main__':
    unittest.main()
