""" modulo de URLS general del proyecto """
#importaciones ---------------------------------------------------------------------------
#django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


#urls ---------------------------------------------------------------------------
urlpatterns = [

    path('admin/', admin.site.urls),
    #urls apps -------------------------


]  #archivos estáticos
