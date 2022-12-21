from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class AppUserCreateForm(auth_forms.UserCreationForm):
    GEN_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    ENG_TYPE = [
        ('MECHANICAL', 'Mechanical'),
        ('ELECTRICAL', 'Electrical'),
        ('INDUSTRIAL', 'Industrial'),
        ('CHEMICAL', 'Chemical'),
        ('CIVIL', 'Civil'),
        ('SOFTWARE', 'Software'),
    ]

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'email', 'password1', 'password2', 'age', 'gender', 'eng_type',
                  'university', 'workplace')
        field_classes = {
            'username': auth_forms.UsernameField
        }
        #TODO: placeholders JS if time

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'age': 'Age',
            'gender': 'Gender',
            'eng_type': 'Type of your education',
            'university': 'University',
            'workplace': 'Workplace',

        }


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'age', 'gender', 'eng_type', 'university', 'workplace')
        field_classes = {'username': auth_forms.UsernameField}
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'age': 'Age',
            'gender': 'Gender',
            'eng_type': 'Type of your education',
            'university': 'University',
            'workplace': 'Workplace',

        }


