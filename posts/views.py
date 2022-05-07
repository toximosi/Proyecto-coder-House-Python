"""Posts Vistas"""
# bibliografia: ---------------------------------------------------------
    # http://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/CreateView/
    # http://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/FormView/
    # http://ccbv.co.uk/projects/Django/4.0/django.views.generic.edit/UpdateView/
# importaciones ---------------------------------------------------------
# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


# code -------------------------------------------------------------------
class PostsFeedView(LoginRequiredMixin, ListView):
    """ Devuelve todos las publicaciones """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30 #paginar
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """ Devuelve el detalle de la publicación """

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Crea un nuevo post """

    template_name = 'posts/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
