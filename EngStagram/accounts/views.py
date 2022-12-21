from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from EngStagram.accounts.forms import AppUserCreateForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = AppUserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()

        photos = self.object.photo_set.order_by('publication_date')

        paginator = Paginator(photos, self.photos_paginate_by)

        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['is_owner'] = self.request.user == self.object
        context['projects_count'] = self.object.project_set.count()
        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        context['photos'] = self.get_paginated_photos()
        context['projects'] = self.object.project_set.all()

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    # form_class = UserEditForm
    fields = ('first_name','last_name','email', 'age', 'gender', 'eng_type', 'workplace', 'university',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


