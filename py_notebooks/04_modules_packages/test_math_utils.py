# test_math_utils.py

import unittest
from math_utils import add, area_circle, PI

class TestMathUtils(unittest.TestCase):

    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.2), 5.7)

    def test_area_circle_zero_radius(self):
        self.assertEqual(area_circle(0), 0)

    def test_area_circle_positive_radius(self):
        self.assertAlmostEqual(area_circle(1), PI * 1 * 1)

    def test_area_circle_float_radius(self):
        r = 2.5
        expected = PI * r ** 2
        self.assertAlmostEqual(area_circle(r), expected)

if __name__ == '__main__':
    unittest.main()