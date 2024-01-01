from flasgger import Schema, fields, ValidationError

from marshmallow import validates, post_load

from models import get_book_by_title, Book, Author
class BookSchema(Schema):

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author_id = fields.Int(required=True)

    @validates('title')
    def validate_title(self, title: str) -> None:
        if get_book_by_title(title) is not None:
            raise ValidationError(f"Book with title {title} is already exists, please use a different title")

    @post_load
    def create_book(self, data, **kwargs) -> Book:
        return Book(**data)


class AuthorSchema(Schema):

    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    middle_name = fields.Str(required=False)

    @post_load
    def create_author(self, data, **kwargs) -> Author:
        return Author(**data)
