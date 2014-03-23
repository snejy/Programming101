import unittest
import solution

class TestSevensInARow(unittest.TestCase):
    def test_with_3(self):
        self.assertEqual(True, solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))

    def test_with_false(self):
        self.assertEqual(False, solution.sevens_in_a_row([1,7,1,7,7], 4))

    def test_with_empty_array(self):
        self.assertEqual(False, solution.sevens_in_a_row([],1))

    def test_with_empty_arr(self):
        self.assertEqual(True, solution.sevens_in_a_row([],0))

if __name__ == '__main__':
    unittest.main()