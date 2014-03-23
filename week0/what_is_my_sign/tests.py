import unittest
import solution


class TestWhatIsMySign(unittest.TestCase):
    def test_for_leo(self):
        self.assertEqual("Leo", solution.what_is_my_sign(5, 8))

    def test_for_taurus(self):
        self.assertEqual("Taurus", solution.what_is_my_sign(3, 5))

    def test_for_aquarius(self):
        self.assertEqual("Aquarius", solution.what_is_my_sign(29, 1))

    def test_for_cancer(self):
        self.assertEqual("Cancer", solution.what_is_my_sign(30, 6))

    def test_for_gemini(self):
        self.assertEqual("Gemini", solution.what_is_my_sign(31, 5))

    def test_for_aquarius_2(self):
        self.assertEqual("Aquarius", solution.what_is_my_sign(2, 2))

    def test_for_capricorn(self):
        self.assertEqual("Capricorn", solution.what_is_my_sign(9, 1))
if __name__ == '__main__':
    unittest.main()