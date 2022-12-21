from enum import Enum

from django.contrib.auth import models as auth_models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators
from django.db import models

from EngStagram.utils.model_mixins import ChoicesEnumMixin
from EngStagram.utils.validators import validate_only_letters

from EngStagram.accounts.managers import AppUserManager

username_validator = UnicodeUsernameValidator()


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class EngTypes(ChoicesEnumMixin, Enum):
    mechanical = 'Mechanical'
    electrical = 'Electrical'
    industrial = 'Industrial'
    chemical = 'Chemical'
    civil = 'Civil'
    software = 'Software'


class AppUser(auth_models.AbstractUser):
    # TODO: separate auth from user cred if time
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 32
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 32
    MIN_LEN_UNIVERSITY = 2
    MAX_LEN_UNIVERSITY = 64
    MIN_LEN_WORKPLACE = 2
    MAX_LEN_WORKPLACE = 64

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    age = models.PositiveIntegerField(
            null=True,
            blank=True,
    )

    eng_type = models.CharField(
        max_length=EngTypes.max_len(),
        choices=EngTypes.choices(),
        null=True,
        blank=True,
    )

    university = models.CharField(
        max_length=MAX_LEN_UNIVERSITY,
        validators=(
            validators.MinLengthValidator(MIN_LEN_UNIVERSITY),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    workplace = models.CharField(
        max_length=MAX_LEN_WORKPLACE,
        validators=(
            validators.MinLengthValidator(MIN_LEN_WORKPLACE),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

