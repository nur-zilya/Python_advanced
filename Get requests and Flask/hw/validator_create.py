from flask import Field
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, ValidationError
from wtforms import IntegerField
from typing import Optional


def number_length(min: int, max: int, message: Optional[str] = None):

    def _number_length(form: FlaskForm, field: Field):
        if len(field) < min:
            if message:
                raise ValidationError(message)
            else:
                raise ValidationError

        elif len(field) > max:
            if message:
                raise ValidationError(message)
            else:
                raise ValidationError

    return _number_length



# class NumberLength:
#     def __init__(self, min_length, max_length, message=None):
#         self.min_length = min_length
#         self.max_length = max_length
#         self.message = message
#
#     def __call__(self, form, field):
#         length = len(str(field.data))
#         if length < self.min_length or length > self.max_length:
#             if self.message is None:
#                 message = f'Field must be between {self.min_length} and {self.max_length} digits long.'
#             else:
#                 message = self.message
#             raise ValidationError(message)

number = IntegerField(validators=[InputRequired(), NumberLength()])