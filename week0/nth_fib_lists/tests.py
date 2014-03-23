import unittest
import solution


class TestNthFibonacciList(unittest.TestCase):
    def test(self):
        self.assertEqual([1], solution.nth_fib_lists([1], [2], 1))
        self.assertEqual([2], solution.nth_fib_lists([1], [2], 2))
        self.assertEqual([1, 2, 3, 1, 2, 3], solution.nth_fib_lists([], [1, 2, 3], 4))
        self.assertEqual([1, 2, 1, 3], solution.nth_fib_lists([1, 2], [1, 3], 3))
        self.assertEqual([], solution.nth_fib_lists([], [], 100))

if __name__ == '__main__':
    unittest.main()