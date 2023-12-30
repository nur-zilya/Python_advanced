import requests

class BookClient:

    URL = 'http://127.0.0.1:5000/api/books/'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_books(self):
        response = self._session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_book(self, data):
        response = self._session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))