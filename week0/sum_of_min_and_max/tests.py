import unittest

import solution

class TestSum(unittest.TestCase):
    def test_with_0(self):
        self.assertEqual(solution.sum_of_min_and_max([0]),0)

    def test_with_empty_array(self):
        self.assertEqual(solution.sum_of_min_and_max([]),0)

    def test_with_normal_array(self):
        self.assertEqual(solution.sum_of_min_and_max([1,2,3,4,5,6,8,9]),10)

    def test_with_sum_that_equal_0(self):
        self.assertEqual(solution.sum_of_min_and_max([1,-2,0,2]),0)

    def test_with_negative_numbers(self):
        self.assertEqual(solution.sum_of_min_and_max([-1,-2,-3,-4,-2,-8,-1]),-9)

    def test_with_negative_and_positive_numbers(self):
        self.assertEqual(solution.sum_of_min_and_max([-10,5,10,100]),90)

if __name__ == '__main__':
    unittest.main()