import unittest
from freezegun import freeze_time

from CI_basics.previous_hw.have_a_good_day import app, hello
from datetime import datetime


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello_world/'

    def test_can_get_correct_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_get_correct_username_with_weekdate(self):
        username = 'Хорошей среды'
        weekday = datetime.today().weekday()
        with freeze_time("2023-04-28"):
            expected_weekday = 4  # 4 corresponds to Friday
            response = hello(username)
            response_text = response
            self.assertTrue(f"Хорошей пятницы" in response_text)
            self.assertEqual(weekday, expected_weekday)

    def test_can_handle_good_day_greeting(self):
        username = 'Хорошего дня'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        expected_response = 'Привет, Хорошего дня. Хорошего Воскресенья!'
        self.assertEqual(response_text, expected_response)


if __name__ == "__main__":
    unittest.main()
