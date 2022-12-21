from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from EngStagram.utils.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Project(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_LEN_NAME = 30

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_start = models.DateField(
        null=True,
        blank=True,
    )

    expected_date_of_end = models.DateField(
        null=True,
        blank=True,
    )

    ended_date = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)