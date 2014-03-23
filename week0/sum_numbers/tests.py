import unittest
import solution
import os

class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.filename = 'test.txt'
        self.file_handler = open(self.filename, 'w')
        self.file_handler.write('11 11 11')
        self.file_handler.close()

    def test_sum_numbers(self):
        self.assertEqual(33, solution.sum_numbers(self.filename))

    def tearDown(self):
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()