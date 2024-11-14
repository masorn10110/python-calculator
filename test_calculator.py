import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # correct
        self.assertEqual(self.calc.add(5, 3), 8) # correct

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 5), -3) # before edit return 3, now correct
        self.assertEqual(self.calc.subtract(3, 1), 2) # before edit return -2, now correct

    def test_mul(self):
        self.assertEqual(self.calc.multiply(5, -1), -5) # before edit return 0, now correct
        self.assertEqual(self.calc.multiply(-2, -5), 10) # before edit return 12, now correct
    
    def test_div(self):
        self.assertEqual(self.calc.divide(5, 0), ZeroDivisionError) # before edit loop deadlock, now correct
        self.assertEqual(self.calc.divide(-4, -2), 2) # before edit loop deadlock, now correct
        
    def test_mod(self):
        self.assertEqual(self.calc.modulo(5, 0), ZeroDivisionError) # before edit loop deadlock, now correct
        self.assertEqual(self.calc.modulo(-9, -2), -1) # before edit return -3, now correct

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()