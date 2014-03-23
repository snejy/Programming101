import unittest
import solution


class TestPrimeFactorization(unittest.TestCase):
    def test_with_prime_number(self):
        self.assertEqual([(89, 1)], solution.prime_factorization(89))

    def test_with_10(self):
        self.assertEqual([(2, 1), (5, 1)], solution.prime_factorization(10))

    def test_with_14(self):
        self.assertEqual([(2, 1), (7, 1)], solution.prime_factorization(14))

    def test_with_356(self):
        self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))

    def test_with_1000(self):
        self.assertEqual([(2, 3), (5, 3)], solution.prime_factorization(1000))


if __name__ == '__main__':
    unittest.main()