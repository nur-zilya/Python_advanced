import unittest

from social_age import get_social_status

class TestSocialAge(unittest.TestCase):

    def test_can_get_child_age(self):
        age = 0
        expected_res = 'child'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_teenager_age(self):
        age = 0
        expected_res = 'teenager'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_adult_age(self):
        age = 0
        expected_res = 'adult'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_senior_age(self):
        age = 0
        expected_res = 'senior'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_retiree_age(self):
        age = 0
        expected_res = 'retiree'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_cannot_pass_negative_number_as_age(self):
        age = -1
        with self.assertRaises(ValueError):
            get_social_status(age)