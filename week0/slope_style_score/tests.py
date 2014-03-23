import unittest
import solution


class TestSlopeStyleScore(unittest.TestCase):
    def test_with_3_elements(self):
        self.assertEqual(2.0, solution.slope_style_score([1,80,2]))

    def test_with_float_average(self):
        self.assertEqual(94.66, solution.slope_style_score([94, 95, 95, 95, 90]))

    def test_1(self):
        self.assertEqual(80.0, solution.slope_style_score([60, 70, 80, 90, 100]))

    def test_2(self):
        self.assertEqual(93.5, solution.slope_style_score([96, 95.5, 93, 89, 92]))

if __name__ == '__main__':
    unittest.main()