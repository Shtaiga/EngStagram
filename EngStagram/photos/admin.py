from django.contrib import admin

from EngStagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'project')

    @staticmethod
    def project(current_photo_obj):
        if current_photo_obj:
            return current_photo_obj.tagged_projects_id
        return 'No projects'
