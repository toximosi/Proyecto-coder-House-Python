""" Post de URLS """
#code ---------------------------------------------------------------------------
from django.contrib import admin
from django.urls import path, include


#urls ---------------------------------------------------------------------------
urlpatterns = [
    #url para acceder a admin: ejem: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),
    
    #urls apps -------------------------
    #path('post/', include('posts.urls')),

]