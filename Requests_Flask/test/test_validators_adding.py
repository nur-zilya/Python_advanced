import unittest

from Requests_Flask.validators_adding import app


class TestValidators(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration/'

    def test_valid_email(self):
        data = {'email': 'test@example.com'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400) #correct

        data = {'email': 'notanemail'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400) #incorrect

    def test_valid_phone(self):
        data = {'phone' : '0123456789'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)

        data = {'phone': '23456789'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400) #incorrect

    def test_valid_name(self):
        data = {'name': 'Myname'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400) #correct

        data = {'name': 2}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400) #incorrect

    def test_valid_address(self):
        data = {'address': 'Main Street, 1'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)

        data = {'address': ''}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)

    def test_valid_index(self):
        data = {'index': '123123'}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)

        data = {'index': ''}
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)



if __name__ == "__main__":
    unittest.main()