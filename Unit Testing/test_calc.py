import unittest
import calc


class TestCalc(unittest.TestCase):
    # naming convention indicates that it should start with test_
    # first test
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(2, -2), 0)
        self.assertEqual(calc.add(0, -5), -5)

    # second test
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(2, -2), 4)
        self.assertEqual(calc.subtract(0, -5), 5)

    # third test
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(2, -2), -4)
        self.assertEqual(calc.multiply(0, -5), 0)

    # fourth test
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(2, -2), -1)
        self.assertEqual(calc.divide(0, -5), 0)
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
