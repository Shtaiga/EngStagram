from EngStagram.projects.models import Project

def get_project_by_name_and_username(project_slug, username):
    return Project.objects.filter(slug=project_slug, user__username=username ).get()