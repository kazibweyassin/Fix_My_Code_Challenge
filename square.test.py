import unittest
from square import square

class SquareTests(unittest.TestCase):
    def setUp(self):
        self.s = square(width=12, height=9)

    def test_area_of_my_square(self):
        self.assertEqual(self.s.area_of_my_square(), 144)

    def test_perimeter_of_my_square(self):
        self.assertEqual(self.s.Perimiter_of_my_square(), 42)

    def test_string_representation(self):
        self.assertEqual(str(self.s), "12/9")

if __name__ == "__main__":
    unittest.main()