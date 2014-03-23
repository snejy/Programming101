import unittest
import solution

class TestPrimeNumberOfDivisors(unittest.TestCase):
    def test_with_7(self):
        self.assertEqual(True, solution.prime_number_of_divisors(7))

    def test_with_8(self):
        self.assertEqual(False, solution.prime_number_of_divisors(8))

    def test_with_9(self):
        self.assertEqual(True, solution.prime_number_of_divisors(9))

    def test_with_0(self):
        self.assertEqual(False, solution.prime_number_of_divisors(0))

    def test_with_1(self):
        self.assertEqual(False, solution.prime_number_of_divisors(1))

    def test_with_2(self):
        self.assertEqual(True, solution.prime_number_of_divisors(2))

if __name__ == '__main__':
    unittest.main()