import unittest
import solution

class TestCountingSubstrings(unittest.TestCase):
    def test_with_two_digit_substring(self):
        self.assertEqual(2, solution.count_substrings("This is a test string", "is"))

    def test_with_equal_substring(self):
        self.assertEqual(2, solution.count_substrings("babababa", "baba"))

    def test_with_one_symbol(self):
        self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))

    def test_with_no_matches(self):
        self.assertEqual(0, solution.count_substrings("We have nothing in common!", "really?"))

    def test_with_lowercase_word(self):
        self.assertEqual(2, solution.count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    unittest.main()