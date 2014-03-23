import unittest
import solution


class TestCountVowels(unittest.TestCase):
    def test_with_one_word(self):
        self.assertEqual(2, solution.count_vowels("Python"))

    def test_with_many_vowels(self):
        self.assertEqual(8, solution.count_vowels("Theistareykjarbunga"))

    def test_with_uppercase_vowels(self):
        self.assertEqual(8, solution.count_vowels("A nice day to code!"))

    def test_with_only_uppercase(self):
        self.assertEqual(5, solution.count_vowels("AMAZING TIME!!!"))

    def test_with_long_sentence(self):
        self.assertEqual(22, solution.count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_with_no_vowels(self):
        self.assertEqual(0, solution.count_vowels("RRgRgrrgrgrrhhtttp!"))

if __name__ == '__main__':
    unittest.main()