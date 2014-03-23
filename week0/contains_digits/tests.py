import unittest
import solution


class TestContainsDigits(unittest.TestCase):
    def test_with_empty_array(self):
        self.assertEqual(True, solution.contains_digits(456, []))

    def test_with_false(self):
        self.assertEqual(False, solution.contains_digits(42123, [0, 3, 4]))

    def test_with_true(self):
        self.assertEqual(True, solution.contains_digits(402123454, [0, 3, 4]))

    def test_with_another(self):
        self.assertEqual(False, solution.contains_digits(123456789, [1,2,3,0]))

    def test_with_repeated_elements(self):
        self.assertEqual(False, solution.contains_digits(666, [6,4]))

if __name__ == '__main__':
    unittest.main()