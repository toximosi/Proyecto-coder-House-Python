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


#urls ---------------------------------------------------------------------------
urlpatterns = [
    #url para acceder a admin: ejem: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),
    #urls apps -------------------------


]  #archivos estáticos