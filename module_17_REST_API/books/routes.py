from dataclasses import asdict

from flask_restful import Api, Resource
from flask import Flask

from models import (
    DATA,
    get_all_books,
    init_db
)

app = Flask(__name__)
api = Api(app)

class BookList(Resource):
    def get(self):
        return {'data': [asdict(book) for book in get_all_books()]}, 200

api.add_resource(BookList, '/api/books')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)