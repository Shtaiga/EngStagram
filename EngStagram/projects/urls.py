from django.urls import path, include

from EngStagram.projects.views import add_project, details_project, edit_project, delete_project

urlpatterns = (
    path('add/', add_project, name='add project'),
    path('<str:username>/project/<slug:project_slug>/', include([
        path('', details_project, name='details project'),
        path('edit/', edit_project, name='edit project'),
        path('delete/', delete_project, name='delete project'),
    ]))
)

