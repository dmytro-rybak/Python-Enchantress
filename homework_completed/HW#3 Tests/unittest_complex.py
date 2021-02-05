import unittest
from homework.tests_complex import *
from unittest import mock


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.test = Test()
        self.test.__enter__()

    def tearDown(self):
        self.test.__exit__(None, None, None)

    def test_enter_function(self):
        self.assertEqual(self.test.__enter__(), self.test)

    def test_exit_function(self):
        self.assertEqual(self.test.__exit__(None, None, None), None)

    def test_hello_function(self):
        self.assertEqual(self.test.hello(), 1)

    def test_new_test_function(self):
        self.assertIsInstance(new_test(), Test)

    def test_func(self):
        self.assertEqual(func(), self.test.hello())

    def test_func_mocked(self):
        with mock.patch("homework.tests_complex.Test.hello") as mocked_hello:
            mocked_hello.return_value = "hello from mock"
            new_func = func()
            self.assertEqual(new_func, "hello from mock")


if __name__ == '__main__':
    unittest.main()
