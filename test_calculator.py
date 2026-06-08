import unittest
from calculator import add

class TestCalculatorAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 1), 2)
        
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        
    def test_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()