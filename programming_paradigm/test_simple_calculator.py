import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test__subtract(self):
        '''Test subtraction methode.'''
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, -1), 2)

    def test__multiply(self):
        '''Test multiplication methode.'''
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test__divide(self):
        '''Test division methode.'''
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(1, 0), None)


if __name__ == "__main__":
    unittest.main()