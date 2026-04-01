from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        value = field.data
        if value is None:
            return

        length = len(str(value))
        if length < min or length > max:
            raise ValidationError(message or f"Некорректная длина номера телефона")

    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        value = field.data
        if value is None:
            return

        length = len(str(value))
        if length < self.min or length > self.max:
            raise ValidationError(
                self.message or f"Некорректная длина номера телефона"
            )
