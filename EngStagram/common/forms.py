from django import forms

from EngStagram.common.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchPhotoForm(forms.Form):
    SEARCH_NAME_MAX_LENGTH = 50
    project_name = forms.CharField(
        max_length=SEARCH_NAME_MAX_LENGTH,
        required=False,
    )