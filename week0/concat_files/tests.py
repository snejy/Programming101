import unittest
import solution
import os

class TestConcatFiles(unittest.TestCase):
    def setUp(self):
        self.filename1 = 'test1.txt'
        self.filename2 = 'test2.txt'
        self.file_handler1 = open(self.filename1, 'w')
        self.file_handler2 = open(self.filename2, 'w')
        self.file_handler1.write("test1")
        self.file_handler2.write("test2")
        self.file_handler1.close()
        self.file_handler2.close()
        self.array = [self.filename1, self.filename2]

    def test_concat_files(self):
        self.assertEqual('test1\ntest2\n', solution.concat_files(self.array))

    def tearDown(self):
        os.remove(self.filename1)
        os.remove(self.filename2)

if __name__ == '__main__':
    unittest.main()