from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('EngStagram.accounts.urls')),
    path('', include('EngStagram.common.urls')),
    path('projects/', include('EngStagram.projects.urls')),
    path('photos/', include('EngStagram.photos.urls')),
]
