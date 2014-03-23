import unittest
import solution


class TestGoldbach(unittest.TestCase):
    def test(self):
        self.assertEqual([(2,2)], solution.goldbach(4))
        self.assertEqual([(3,3)], solution.goldbach(6))
        self.assertEqual([(3,5)], solution.goldbach(8))
        self.assertEqual([(3,7), (5,5)], solution.goldbach(10))
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], solution.goldbach(100))

if __name__ == '__main__':
    unittest.main()