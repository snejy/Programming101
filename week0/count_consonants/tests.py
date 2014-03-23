import unittest
import solution


class TestCountVowels(unittest.TestCase):
    def test_with_one_word(self):
        self.assertEqual(4, solution.count_consonants("Python"))

    def test_with_many_consonants(self):
        self.assertEqual(11, solution.count_consonants("Theistareykjarbunga"))

    def test_with_uppercase_consonants(self):
        self.assertEqual(6, solution.count_consonants("A nice day to code!"))

    def test_with_only_uppercase(self):
        self.assertEqual(6, solution.count_consonants("AMAZING TIME!!!"))

    def test_with_long_sentence(self):
        self.assertEqual(44, solution.count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_with_consonants(self):
        self.assertEqual(18, solution.count_consonants("RRgRgrrgrgrrhhtttp!"))

    def test_with_no_consonants(self):
        self.assertEqual(0, solution.count_consonants("AaaaIIIaaiaIAIiAyAuayA"))

if __name__ == '__main__':
    unittest.main()