import pyperclip

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import get_user_model

from EngStagram.common.forms import SearchPhotoForm, PhotoCommentForm
from EngStagram.common.models import PhotoLike
from EngStagram.common.utils import get_photo_url
from EngStagram.photos.models import Photo
from EngStagram.utils.photo_utils import apply_likes_count, apply_user_liked_photo

UserModel = get_user_model()


def index(request):
    search_form = SearchPhotoForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['project_name']

    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_projects__name__icontains=search_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
        'is_owner': request.user.pk,
    }

    return render(request, 'common/home-page.html', context,)


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects\
        .filter(photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    #TODO: try to make real share app
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })

    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(id=photo_id).get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.user = request.user
        comment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
