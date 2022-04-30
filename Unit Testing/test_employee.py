import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # runs before everything
    @classmethod
    def setUpClass(cls):
        print('setUp class\n')

    # runs after everything
    @classmethod
    def terDownClass(cls):
        print('tearDown class\n')

    # runs code before every single test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # runs code after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('testEmail')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.last = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Jane@email.com')

    def test_fullname(self):
        print('testFullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.last = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Jane')

    def test_apply_raise(self):
        print('testApplyRaise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
