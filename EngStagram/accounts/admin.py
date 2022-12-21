from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from EngStagram.accounts.forms import AppUserCreateForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = AppUserCreateForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'email',
                    'password',
                ),
            }),

        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'gender',
                    'age',
                    'eng_type',
                    'workplace',
                    'university',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)