from django.contrib import admin

from EngStagram.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
