import unittest
import solution


class TestIntPalindrome(unittest.TestCase):
    def test_with_one_digit_number(self):
        self.assertEqual(True, solution.is_int_palindrome(1))

    def test_with_two_different_digits(self):
        self.assertEqual(False, solution.is_int_palindrome(42))

    def test_with_three_different_digits(self):
        self.assertEqual(False, solution.is_int_palindrome(123))

    def test_with_two_equal_third_not_digits(self):
        self.assertEqual(False, solution.is_int_palindrome(112))

    def test_with_three_equal_digits(self):
        self.assertEqual(True, solution.is_int_palindrome(111))

    def test_with_many_digits_number(self):
        self.assertEqual(True, solution.is_int_palindrome(1000001))

if __name__ == '__main__':
    unittest.main()