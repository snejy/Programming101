import unittest
import solution

class TestBiggestDifference(unittest.TestCase):
    def test_with_one_number_array(self):
        self.assertEqual(0, solution.biggest_difference([1]))

    def test_with_two_numbers_array(self):
        self.assertEqual(-2, solution.biggest_difference([1,3]))

    def test_with_long_array(self):
        self.assertEqual(-4, solution.biggest_difference([1,2,3,4,5]))

    def test_with_only_negative_numbers(self):
        self.assertEqual(-9, solution.biggest_difference([-10, -9, -1]))

    def test_with_range(self):
        self.assertEqual(-99, solution.biggest_difference(range(100)))

if __name__ == '__main__':
    unittest.main()        