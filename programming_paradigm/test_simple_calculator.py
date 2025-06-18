import unittest 
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
        def test_addition(self):
            self.assertEqual(self.calc.add(2, 3, 5))
            self.assetEqual(self.calc.add(-1,1,0))
        def test_subtract(self):
            self.assertEqual(self.calc.subtract(2,3,5))
            self.assertEqual(self.Calc.subtract(-1,1,0))
        def test_multiplication(self):
            self.assertEqual(self.calc.multiply(2,3,5))
            self.assertEqual(self.calc.multiply(-1,1,0))
        def test_divide(self):
            self.assertEqual(self.calc.divide(2,3,5))
            self.assertEqual(self.calc.divide(-1,1,0))
