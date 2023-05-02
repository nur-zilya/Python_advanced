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
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        with freeze_time("2023-04-28"):
            result = hello(username)
            self.assertTrue("Хорошей пятницы" in response_text)
