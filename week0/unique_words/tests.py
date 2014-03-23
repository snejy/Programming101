import unittest
import solution

class TestUniqueWordsCount(unittest.TestCase):
    def test_with_one_unique_word(self):
        self.assertEqual(1, solution.unique_words_count(["HELLO!"] * 10))

    def test_with_two_unique_words(self):
        self.assertEqual(2, solution.unique_words_count(["python", "python", "python", "ruby"]))

    def test_with_3_unique_words(self):
        self.assertEqual(3, solution.unique_words_count(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    unittest.main()