import unittest
import solution

class TestIsPrime(unittest.TestCase):
    def test_with_0(self):
        self.assertEqual(False, solution.is_prime(0))

    def test_with_1(self):
        self.assertEqual(False, solution.is_prime(1))

    def test_with_2(self):
        self.assertEqual(True, solution.is_prime(2))

    def test_with_negative_prime(self):
        self.assertEqual(True, solution.is_prime(-3))

    def test_with_negative_nonprime(self):
        self.assertEqual(False, solution.is_prime(-10))

    def test_with_random_prime(self):
        self.assertEqual(True, solution.is_prime(11))

    def test_with_random_nonprime(self):
        self.assertEqual(False, solution.is_prime(1002))

if __name__ == '__main__':
    unittest.main()