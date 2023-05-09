import unittest

from Requests_Flask import flask_wtforms
from Requests_Flask.flask_wtforms import app


class TestPersonalData(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration/'

    def test_missing_email(self):
        response = self.app.post("/registration", data={"phone": "1234567890", "name": "John D. O."})
        self.assertEqual(response.status_code, 400)

    def test_missing_phone(self):
        response = self.app.post("/registration", data={"name": "Lu-Salome", "email" : "salomela@google.com"})
        self.assertEqual(response.status_code, 400)

    def test_missing_name(self):
        response = self.app.post("/registration", data={"phone" : "88888888", "email" : "salomela@google.com"})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()