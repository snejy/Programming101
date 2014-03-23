import unittest
import solution


class TestIsAnBn(unittest.TestCase):
    def test_with_empty_string(self):
        self.assertEqual(True, solution.is_an_bn(""))

    def test_with_false(self):
        self.assertEqual(False, solution.is_an_bn("rado"))
        self.assertEqual(False, solution.is_an_bn("aaabb"))
        self.assertEqual(False, solution.is_an_bn("aabbaabb"))
        self.assertEqual(False, solution.is_an_bn("bbbaaa"))

    def test_with_true(self):
        self.assertEqual(True, solution.is_an_bn("aaabbb"))
        self.assertEqual(True, solution.is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()