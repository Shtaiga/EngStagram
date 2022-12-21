from django import forms

from EngStagram.common.models import PhotoLike, PhotoComment
from EngStagram.photos.models import Photo
from EngStagram.utils.form_mixins import DisabledFormMixin


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(PhotoBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_projects.clear()

            Photo.objects.all().first().tagged_projects.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()

        return self.instance
