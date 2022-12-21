from django.contrib import admin

from EngStagram.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
