import unittest

from Linux_2.homework.remote_execute import app


class TestRemoteCode(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/execute_code/'

    def test_missing_code(self):
        response = self.app.post("/execute_code", data={"time_out": 9})
        self.assertEqual(response.status_code, 400)

    def test_missing_time_out(self):
        response = self.app.post("/execute_code", data={"code": "print('Hello, world!')"})
        self.assertEqual(response.status_code, 400)

    def test_invalid_time_out(self):
        response = self.app.post("/execute_code", data={"code": "print('Hello, world!')", "time_out": -1})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'error': 'Invalid input data'})

    def test_execution_timeout(self):
        response = self.app.post("/execute_code", data={'code': 'import time\nwhile True:\n    time.sleep(1)', 'timeout': 1})
        self.assertEqual(response.status_code, 408)
        self.assertEqual(response.json(), {'error': 'Execution timeout'})

    def test_shell_injection(self):
        response = self.app.post("/execute_code", data={'code': 'print("hello world!")"; echo "hacked', 'timeout': 5})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'error': 'Invalid input data'})

    if __name__ == '__main__':
        unittest.main()