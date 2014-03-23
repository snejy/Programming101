import unittest
import solution


class TestIsNumberBalanced(unittest.TestCase):
    def test_with_one_digit(self):
        self.assertEqual(True, solution.is_number_balanced(9))

    def test_with_two_digits_not_balanced(self):
        self.assertEqual(False, solution.is_number_balanced(12))

    def test_with_two_digits_balanced(self):
        self.assertEqual(True, solution.is_number_balanced(11))

    def test_with_3_digits(self):
        self.assertEqual(True, solution.is_number_balanced(121))

    def test_with_3_digits_false(self):
        self.assertEqual(False, solution.is_number_balanced(112))

    def test_with_many_digits(self):
        self.assertEqual(True, solution.is_number_balanced(1238033))

    def test_with_many_digit_not_balanced(self):
        self.assertEqual(False, solution.is_number_balanced(28471))

if __name__ == '__main__':
    unittest.main()