import unittest
import solution


class TestIsSequenceIncreasing(unittest.TestCase):
    def test_with_one_element(self):
        self.assertEqual(True, solution.is_increasing([1]))

    def test_with_increasing_seq(self):
        self.assertEqual(True, solution.is_increasing([1, 2, 3, 4]))

    def test_with_equal_elements(self):
        self.assertEqual(False, solution.is_increasing([1, 1, 1]))

    def test_with_not_increasing_seq(self):
        self.assertEqual(False, solution.is_increasing([1, 2, 3, 1]))

    def test_with_negative_numbers(self):
        self.assertEqual(True, solution.is_increasing([-10, -9, -8]))

    def test_with_negative_and_positive_numbers(self):
        self.assertEqual(False, solution.is_increasing([-3, 2 , 10, -2]))

if __name__ == '__main__':
    unittest.main()