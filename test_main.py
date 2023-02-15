from unittest import TestCase

from main import add


class some_tests(TestCase):
    def test_add_function_1(self):
        result = add(1, 1)
        self.assertEqual(result, 2)

    def test_add_function_2(self):
        with self.assertRaises(TypeError):
            add(1, 'a')
