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
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post
from users.models import Profile


# code -------------------------------------------------------------------
class PostsFeedView(ListView):#class PostsFeedView(LoginRequiredMixin, ListView):
    """ Devuelve todos las publicaciones """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)#ordena los post según su creación
    paginate_by = 30 #paginar
    context_object_name = 'posts'
    

# *CRUD: CBV -- mediante DJANGO -------------------------------------------
class postLV(ListView):
    model = Post
    template_name = "post/post_list.html"

# Read: Lectura ----------------------------------
class PostDetailView(DetailView): #class PostDetailView(LoginRequiredMixin, DetailView):
    """ Devuelve el detalle de la publicación """
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

# Create: Crear ----------------------------------
class CreatePostView(CreateView): #class CreatePostView(LoginRequiredMixin, CreateView):
    """ Crea un nuevo post """

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

# Delete: Borrar --------------------------------------
""" class postDeV(DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"
    success_url = "/post/list" """

# Update: Actualizar ----------------------------------
""" class postUV(UpdateView):
    model = Post
    template_name = "post/post_form.html"
    sucess_url = "/App/post/list"
    fields = ["titulo", "subtitulo", "image", "cuerpo", "autor", "fecha"] """


