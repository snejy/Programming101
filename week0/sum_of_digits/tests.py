import unittest

import solution

class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_0(self):
        self.assertEqual(solution.sum_of_digits(0),0)

    def test_sum_of_1(self):
        self.assertEqual(solution.sum_of_digits(1),1)

    def test_sum_of_6(self):
        self.assertEqual(solution.sum_of_digits(6),6)

    def test_sum_of_123(self):
        self.assertEqual(solution.sum_of_digits(123),6)

    def test_sum_of_negativenumber(self):
        self.assertEqual(solution.sum_of_digits(-10),1)

    def test_sum_of_another_negativenumber(self):
        self.assertEqual(solution.sum_of_digits(-123),6)

    def test_sum_of_1325132435356(self):
        self.assertEqual(solution.sum_of_digits(1325132435356),43) 

if __name__ == '__main__':
    unittest.main()