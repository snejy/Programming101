import unittest
import solution

class TestContainsDigit(unittest.TestCase):
    def test_with_equal_numbers(self):
        self.assertEqual(True, solution.contains_digit(0, 0))

    def test_with_true(self):
        self.assertEqual(True, solution.contains_digit(1000, 0))

    def test_with_false(self):
        self.assertEqual(False, solution.contains_digit(1234678, 5))

    def test_with_small_number(self):
        self.assertEqual(False, solution.contains_digit(41, 2))

if __name__ == '__main__':
    unittest.main()