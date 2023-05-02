import unittest

from CI_basics.previous_hw.max_num import app


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] =True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/max_number/'

    def cam_get_max_number(self):
        numbers = 3, 5
        url = self.base_url + '/'.join(str(i) for i in numbers)
        response = self.app.get(url)
        response_text = response.data.decode()
        correct_answer_str = f'<i>{max(numbers)}</i>'
        self.assertTrue(correct_answer_str in response_text)