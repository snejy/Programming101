import unittest
import solution
import os

class TestGenerateNumbers(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.file_handler = open(self.filename, 'w')
        solution.generate_numbers(self.filename, 2)
        self.file_handler.close()
        self.file_handler2 = open(self.filename, 'r')
        self.content = self.file_handler2.read()
        self.file_handler2.close()

    def test_generate_numbers(self):
        self.assertEqual(2, len(self.content.split()))

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()