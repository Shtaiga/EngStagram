from django.core import exceptions


def validate_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')