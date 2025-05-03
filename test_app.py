import unittest
from app import suma, resta, multiplicacion, division

class TestApp(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
    
    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
        self.assertEqual(resta(1, 1), 0)
        self.assertEqual(resta(0, 5), -5)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-2, 3), -6)
        self.assertEqual(multiplicacion(0, 5), 0)
    
    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(0, 5), 0)
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()