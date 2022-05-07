""" modulo de URLS general del proyecto """
#bibliografia ----------------------------------------------------
# https://github.com/django/django
# https://docs.djangoproject.com/en/4.0
#importaciones ---------------------------------------------------
#django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#Views
from posts import views as posts_views
from users import views as users_views

#urls ---------------------------------------------------------------------------
urlpatterns = [
    #url para acceder a admin: ejem: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),#user:administrador; pass:Quieroentrar-77
    #urls apps -------------------------
    path('', include(('posts.urls', 'posts'), namespace='posts')),#include para incluir la lista de urls de post
    path('users/', include(('users.urls', 'users'), namespace='users')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#archivos estáticos, le suma una url 