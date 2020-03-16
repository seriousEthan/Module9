# Ethan Martin
# Module 9 Test


import unittest
import module9


class TestMod9(unittest.TestCase):

    def test_add(self):
        self.assertEqual(module9.add(6, 9), 15)
        self.assertEqual(module9.add(-6, 9), 3)
        self.assertEqual(module9.add(-6, -9), -15)

    def test_subtract(self):
        self.assertEqual(module9.subtract(6, 9), -3)
        self.assertEqual(module9.subtract(-6, 9), -15)
        self.assertEqual(module9.subtract(-6, -9), 3)

    def test_multiply(self):
        self.assertEqual(module9.multiply(6, 9), 54)
        self.assertEqual(module9.multiply(-6, 9), -54)
        self.assertEqual(module9.multiply(-6, -9), 54)

    def test_divide(self):
        self.assertEqual(module9.divide(10, 2), 5)
        self.assertEqual(module9.divide(-6, 2), -3)
        self.assertEqual(module9.divide(-6, -2), 3)
        self.assertEqual(module9.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            module9.divide(10, 0)

    def test_c2f(self):
        self.assertEqual(module9.c2f(25), 77)
        self.assertEqual(module9.c2f(0), 32)
        self.assertEqual(module9.c2f(-5), 23)
        self.assertEqual(module9.c2f(-20), -4)

    def test_f2c(self):
        self.assertEqual(module9.f2c(77), 25)
        self.assertEqual(module9.f2c(32), 0)
        self.assertEqual(module9.f2c(23), -5)
        self.assertEqual(module9.f2c(-4), -20)


if __name__ == '__main__':
    unittest.main()
