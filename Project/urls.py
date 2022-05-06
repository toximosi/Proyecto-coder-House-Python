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
from Project import views as local_views
from posts import views as posts_views

#urls ---------------------------------------------------------------------------
urlpatterns = [
    #url para acceder a admin: ejem: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),#user:administrador; pass:Quieroentrar-77
    #urls apps -------------------------
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#archivos estáticos, le suma una url 