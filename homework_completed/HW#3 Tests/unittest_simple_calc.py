import unittest
from homework.test_simple_calc import add, subtract, multiply, divide


class TestSimpleCalc(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(10, -5), 5)

    def test_subtract_function(self):
        self.assertEqual(subtract(7, 3), 4)
        self.assertEqual(subtract(10, 20), -10)

    def test_multiple_function(self):
        self.assertEqual(multiply(10, 2), 20)
        self.assertEqual(multiply(2.5, 3), 7.5)

    def test_division_function(self):
        self.assertEqual(divide(10, 2), 5.0)
        with self.assertRaises(ValueError):
            divide(4, 0)
        self.assertRaises(ValueError, lambda: divide(5, 0))


if __name__ == '__main__':
    unittest.main()
