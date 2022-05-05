""" modulo de URLS general del proyecto """
#code ---------------------------------------------------------------------------
from django.contrib import admin
from django.urls import path, include


#urls ---------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    #urls apps -------------------------
    path('post/', include('posts.urls')),

]
