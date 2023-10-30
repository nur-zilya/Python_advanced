from dataclasses import asdict

from flask_restful import Api, Resource
from flask import Flask, request

from models import (
    DATA,
    get_all_books,
    add_new_book,
    Book,
    init_db
)

from schemas import BookSchema, ValidationError

app = Flask(__name__)
api = Api(app)

class BookList(Resource):
    def get(self):
        return {'data': [asdict(book) for book in get_all_books()]}, 200

    def post(self):
        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_new_book(book)
        return schema.dump(book), 201


api.add_resource(BookList, '/api/books')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)