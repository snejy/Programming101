import unittest

import solution

class TestSum(unittest.TestCase):
    def test_sum_of_divisors_of_0(self):
        self.assertEqual(solution.sum_of_divisors(0),0)

    def test_sum_of_divisors_of_1(self):
        self.assertEqual(solution.sum_of_divisors(1),1)

    def test_sum_of_divisors_of_prime_7(self):
        self.assertEqual(solution.sum_of_divisors(7),8)

    def test_sum_of_divisors_of_prime_big_number_23(self):
        self.assertEqual(solution.sum_of_divisors(23),24)

    def test_sum_of_divisors_of_1000(self):
        self.assertEqual(solution.
            sum_of_divisors(1000),2340)

if __name__ == '__main__':
    unittest.main()