import unittest
import solution
import os

class TestCat2(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.file_handler = open(self.filename, 'w')
        self.file_handler.write("tests")
        self.file_handler.close()
        self.filename2 = 'test2.txt'
        self.file_handler2 = open(self.filename2, 'w')
        self.file_handler2.write("test2")
        self.file_handler2.close()
        self.array = [self.filename, self.filename2]

    def test_cat2(self):
        self.assertEqual(['tests','test2'], solution.cat2(self.array))

    def tearDown(self):
        os.remove(self.filename)
        os.remove(self.filename2)

if __name__ == '__main__':
    unittest.main()
