import unittest
import solution
import os

class TestCat(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.file_handler = open(self.filename, 'w')
        self.file_handler.write("tests")
        self.file_handler.close()

    def test_cat(self):
        self.assertEqual("tests", solution.cat(self.filename))

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()