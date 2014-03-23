import unittest
import solution


class TestNumberToList(unittest.TestCase):
    def test_with_one_digit_number(self):
        self.assertEqual([1], solution.number_to_list(1))

    def test_with_123(self):
        self.assertEqual([1, 2, 3], solution.number_to_list(123))

    def test_with_eqaul_digits_number(self):
        self.assertEqual([9, 9, 9, 9, 9], solution.number_to_list(99999))

    def test_with_another_number(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], solution.number_to_list(123023))

if __name__ == '__main__':
    unittest.main()