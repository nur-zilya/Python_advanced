from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

from flasgger import APISpec, Swagger
from dataclasses import asdict

from flask_restful import Api, Resource
from flask import Flask, request

from models import (
    DATA,
    get_all_books, update_book_by_id,
    add_new_book, delete_book_by_id,
    Book, get_book_by_id,
    init_db, Author, add_new_author, get_all_books_author,
    delete_books_by_author_id
)

from schemas import BookSchema, ValidationError, AuthorSchema

app = Flask(__name__)
api = Api(app)

spec = APISpec(
    title='BookList',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ]
)

class BookList(Resource):
    def get(self):
        """
       This is an endpoint for obtaining the books list.
       ---
       tags:
         - books
       responses:
          200:
            description: A list of books
            schema:
              type: array
              items:
                $ref: '#/definitions/Book'
       """
        return {'data': [asdict(book) for book in get_all_books()]}, 200

    def post(self):
        """
           This is an endpoint for adding new book.
           ---
           tags:
             - books
           parameters:
             - in: body
               name: new book params
               schema:
                 $ref: '#/definitions/Book'
           responses:
              201:
                description: the book was created
                schema:
                  $ref: '#/definitions/Book'
                example: 'The book was created!'
              400:
                description: Bad request
                schema:
                  type: object
                  properties:
                    message:
                      type: string
           """
        data = request.json

        schema = BookSchema()

        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_new_book(book)
        return schema.dump(book), 201


class Book(Resource):
    def put(self, id: int):
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
            book.id = id
            update_book_by_id(book)
            return schema.dump(book), 200
        except ValidationError as e:
            return e.messages, 400

    def get(self, id: int):
        schema = BookSchema()
        book = get_book_by_id(id)
        return schema.dump(book), 200

    def delete(self, id: int):
        delete_book_by_id(id)
        return {'msg': "ok"}, 200


class AuthorsList(Resource):
    def get(self):
        schema = AuthorSchema()
        authors = []  # Replace with actual logic to get all authors
        return {'data': [asdict(author) for author in authors]}, 200


class Authors(Resource):
    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
            add_new_author(author)
            return schema.dump(author), 200
        except ValidationError as e:
            return e.messages, 400

    def get(self, id: int):
        schema = AuthorSchema()
        author = get_all_books_author(id)
        if author:
            return schema.dump(author), 200
        else:
            return {'msg': 'Author not found'}, 404

    def delete(self, id: int):
        delete_books_by_author_id(id)
        return {'msg': "ok"}, 200

template = spec.to_flasgger(
    app,
    definitions=[BookSchema],
)

swagger = Swagger(app, template=template)

api.add_resource(BookList, '/api/books/')
api.add_resource(Book, '/api/books/<int:id>')
api.add_resource(AuthorsList, '/api/authors/')  # Changed the resource name
api.add_resource(Authors, '/api/authors/<int:id>')


if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)