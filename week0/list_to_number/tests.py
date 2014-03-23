import unittest
import solution


class TestListToNumber(unittest.TestCase):
    def test_with_one_element_list(self):
        self.assertEqual(1, solution.list_to_number([1]))

    def test_with_123(self):
        self.assertEqual(123, solution.list_to_number([1,2,3]))

    def test_with_99999(self):
        self.assertEqual(99999, solution.list_to_number([9, 9, 9, 9, 9]))

    def test_with_long_number(self):
        self.assertEqual(123023, solution.list_to_number([1 ,2 ,3 ,0 ,2 ,3]))

if __name__ == '__main__':
    unittest.main()