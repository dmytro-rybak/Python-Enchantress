import unittest
from unittest import mock
from homework.tests_simple_employee import Employee


class TestSimpleEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.employee1 = Employee("Mike", "Smith", 1000)
        cls.employee2 = Employee("Anna", "Brown", 2000)

    def test_email_function(self):
        self.assertEqual(self.employee1.email, "Mike.Smith@email.com")
        self.assertEqual(self.employee2.email, "Anna.Brown@email.com")

    def test_fullname_function(self):
        self.assertEqual(self.employee1.fullname, "Mike Smith")
        self.assertEqual(self.employee2.fullname, "Anna Brown")

    def test_apply_raise_function(self):
        self.employee1.apply_raise()
        self.employee2.apply_raise()
        self.assertEqual(self.employee1.pay, 1050)
        self.assertEqual(self.employee2.pay, 2100)

    def test_monthly_schedule_function(self):
        with mock.patch("homework.tests_simple_employee.requests.get") as mocked_request:
            mocked_request.return_value.ok = True
            mocked_request.return_value.text = "Good Response!"
            schedule = self.employee1.monthly_schedule("June")
            self.assertEqual(schedule, "Good Response!")

            mocked_request.return_value.ok = False
            schedule = self.employee2.monthly_schedule("July")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == '__main__':
    unittest.main()
