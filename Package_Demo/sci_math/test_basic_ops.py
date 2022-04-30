import unittest
import basic_ops


class TestBasicOps(unittest.TestCase):
    def test_power(self):
        self.assertEqual(basic_ops.power(2, 4), 16)

    def test_remainder(self):
        self.assertEqual(basic_ops.remainder(10, 3), 1)


if __name__ == '__main__':
    unittest.main()
