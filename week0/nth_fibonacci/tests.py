import unittest
import solution

class TestFibonacci(unittest.TestCase):
    def test_with_default_1(self):
        self.assertEqual(solution.nth_fibonacci(1),1)
    
    def test_with_default_2(self):
        self.assertEqual(solution.nth_fibonacci(2),1)

    def test_with_fibonacci_3(self):
        self.assertEqual(solution.nth_fibonacci(3),2)

    def test_with_fibonacci_4(self):
        self.assertEqual(solution.nth_fibonacci(4),3)

    def test_with_fibonacci_5(self):
        self.assertEqual(solution.nth_fibonacci(5),5)

    def test_with_random_fibonacci(self):
        self.assertEqual(solution.nth_fibonacci(10),55)

    def test_with_another_random_fibonacci(self):
        self.assertEqual(solution.nth_fibonacci(12),144)

    def test_with_fibonacci_0(self):
        self.assertEqual(solution.nth_fibonacci(0),None)

if __name__ == '__main__':
    unittest.main()