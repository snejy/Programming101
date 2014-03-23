import unittest
import solution
import os

class TestCountLinesWordsChars(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.file_handler = open(self.filename, 'w')
        self.file_handler.write("blah blah\n")
        self.file_handler.close()

    def test(self):
        self.assertEqual(1, solution.count_lines(self.filename))
        self.assertEqual(2, solution.count_words(self.filename))
        self.assertEqual(10, solution.count_chars(self.filename))

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()