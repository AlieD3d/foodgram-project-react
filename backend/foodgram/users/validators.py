from re import compile

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RegexpStringValidator:
    first_regexp = '[^а-яёА-ЯЁ]+'
    second_regexp = '[^a-zA-Z]+'
    message = (
        'Значение на разных языках или содержит недопустимые символы'
    )

    def __init__(self, first_regexp=None, second_regexp=None):
        if first_regexp is not None:
            self.first_regexp = first_regexp
        if second_regexp is not None:
            self.second_regexp = second_regexp

        self.first_regexp = compile(self.first_regexp)
        self.second_regexp = compile(self.second_regexp)

    def __call__(self, value):
        if self.first_regexp.search(value) and self.second_regexp.search(value):
            raise ValidationError(self.message)


@deconstructible
class MinLenUsernameValidator:
    min_len = 0
    message = 'Значение слишком короткое'

    def __int__(self, min_len=None, message=None):
        if min_len is not None:
            self.min_len = min_len
        if message is not None:
            self.message = message

    def __call__(self, value):
        if len(value) < self.min_len:
            raise ValidationError(self.message)
