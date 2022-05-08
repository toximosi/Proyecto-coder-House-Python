"""Users views"""
#importaciones ---------------------------------------------------------
# Django
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse, reverse_lazy #reverse construye una url
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm


class UserDetailView(DetailView):#class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'#necesitamos un identificador para qle queryset
    slug_url_kwarg = 'username'#como lo llamamos del lado del as url
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()#get_object se encarga de traer los datos
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):#para salvar los datos del formulario
        form.save()
        return super().form_valid(form)

class UpdateProfileView(UpdateView):#class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):#sobreescribimos el método
        return self.request.user.profile

    def get_success_url(self):#sobreescribimos el método
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})#reverse construye una url


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    #recuerda cambiar la redirección de login en Settings del proyecto:
    #https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views


class LogoutView(auth_views.LogoutView):#class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'users/logged_out.html'
