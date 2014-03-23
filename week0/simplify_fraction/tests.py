import unittest
import solution


class TestSimplifyFraction(unittest.TestCase):
    def test(self):
        self.assertEqual((1,3), solution.simplify_fraction((3,9)))
        self.assertEqual((1,7), solution.simplify_fraction((1,7)))
        self.assertEqual((2,5), solution.simplify_fraction((4,10)))
        self.assertEqual((3,22), solution.simplify_fraction((63,462)))

if __name__ == '__main__':
    unittest.main()
