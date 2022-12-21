from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from EngStagram.projects.forms import ProjectCreateForm, ProjectEditForm, ProjectDeleteForm
from EngStagram.utils.photo_utils import apply_likes_count, apply_user_liked_photo
from EngStagram.utils.project_utils import get_project_by_name_and_username
from EngStagram.utils.utils import is_owner


def details_project(request, username, project_slug):
    project = get_project_by_name_and_username(project_slug, username)
    photos = [apply_likes_count(photo) for photo in project.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'project': project,
        'photos_count': project.photo_set.count(),
        'project_photos': photos,
        'is_owner': project.user == request.user,

    }
    print(project)
    return render(request, 'projects/project-details-page.html', context,)


@login_required
def add_project(request):
    if request.method == 'GET':
        form = ProjectCreateForm()
    else:
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'projects/project-add-page.html', context,)


def edit_project(request, username, project_slug):
    project = get_project_by_name_and_username(project_slug, username)

    if not is_owner(request, project):
        return redirect('details pet', username=username, project_slug=project_slug)

    if request.method == 'GET':
        form = ProjectEditForm(instance=project)
    else:
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('details project', username=username, project_slug=project_slug)

    context = {
        'form': form,
        'project_slug': project_slug,
        'username': username,
    }
    return render(request, 'projects/project-edit-page.html', context,)


def delete_project(request, username, project_slug):
    project = get_project_by_name_and_username(project_slug, username)

    if request.method == 'GET':
        form = ProjectDeleteForm(instance=project)
    else:
        form = ProjectEditForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'project_slug': project_slug,
        'username': username,
    }

    return render(request, 'projects/project-delete-page.html', context,)
