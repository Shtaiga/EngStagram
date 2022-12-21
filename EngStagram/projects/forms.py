from django import forms

from EngStagram.projects.models import Project
from EngStagram.utils.form_mixins import DisabledFormMixin


class ProjectBaseForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'personal_photo', 'date_of_start', 'expected_date_of_end', 'ended_date')

        labels = {
            'name': 'Project Name',
            'personal_photo': 'Link to Image',
            'date_of_start': 'Date of project start',
            'expected_date_of_end': 'Expected date of ending',
            'ended_date': 'Date that project ended',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Project name'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
            'date_of_start': forms.DateInput(
                attrs={
                    'placeholder': 'dd/mm/yyyy',
                    'type': 'date',
                }
            ),
            'expected_date_of_end': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'ended_date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
        }


class ProjectCreateForm(ProjectBaseForm):
    pass


class ProjectEditForm(DisabledFormMixin, ProjectBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

class ProjectDeleteForm(DisabledFormMixin, ProjectBaseForm):
    disabled_fields = ('name', 'date_of_start', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance