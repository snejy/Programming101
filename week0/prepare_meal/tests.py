import solution
import unittest


class TestPrepareMeal(unittest.TestCase):
    def test_with_spam(self):
        self.assertEqual(' spam', solution.prepare_meal(3))
        self.assertEqual(' spam spam spam', solution.prepare_meal(27))
        self.assertEqual('', solution.prepare_meal(7))

    def test_with_eggs(self):
        self.assertEqual(' eggs', solution.prepare_meal(5))
        self.assertEqual(' spam and eggs', solution.prepare_meal(15))
        self.assertEqual(' spam spam and eggs', solution.prepare_meal(45))

if __name__ == '__main__':
    unittest.main()