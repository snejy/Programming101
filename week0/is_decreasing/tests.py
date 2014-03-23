import unittest
import solution


class TestIsSequenceDecreasing(unittest.TestCase):
    def test_with_decreasing_seq1(self):
        self.assertEqual(True, solution.is_decreasing([5, 4, 3, 2, 1]))

    def test_with_non_decreasing_seq(self):
        self.assertEqual(False, solution.is_decreasing([12,3,5,2,1]))

    def test_with_one_number_array(self):
        self.assertEqual(True, solution.is_decreasing([1]))

    def test_with_equal_numbers(self):
        self.assertEqual(False, solution.is_decreasing([1,1,1,1]))


if __name__ == '__main__':
    unittest.main()