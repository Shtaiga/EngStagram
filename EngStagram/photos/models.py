from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from cloudinary import models as cloudinary_models

# Create your models here.
from EngStagram.projects.models import Project
from EngStagram.utils.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = cloudinary_models.CloudinaryField(
        null=False,
        blank=True,
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )
    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
    # tagged_projects = models.ManyToOneField(
    #     Project,
    #     blank=True,
    # )
    tagged_projects = models.ForeignKey(
        Project,
        # blank=True,
        on_delete=models.RESTRICT,
    )