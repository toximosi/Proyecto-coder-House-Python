
""" USER model """
"""NOTE:bibliografia:
    https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
    https://docs.djangoproject.com/en/4.0/ref/models/fields/
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
    """
#importaciones ---------------------------------------------------------
#django
from django.db import models
from django.contrib.auth.models import User #heredamos de user de django
# Create your models here.
class Profile(models.Model):#en vez de USER le llamamos Profile por perfil de usuario
    """Profile model 
    modelo Proxy que extiende la base de datos con otra información"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #? on_delete: que hace si se borra el user->en este caso acturá como un SQL
    biography = models.TextField(blank=True) 
    phone_number = models.CharField(max_length=20, blank=True)
    #? blank=True, que permite que se quede vacio
    website = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True )#!Necesario instalar pip install Pillowq
    #upload_to: donde se guardarán las imágenes
    created = models.DateTimeField(auto_now_add=True)#fechas de creación 
    modified = models.DateTimeField(auto_now=True)#fecha de modificación 
    
    def __str__(self): #representacion en string en admin
        return f"user: {self.user} - biography: {self.biography} - website: {self.website} - picture: {self.picture} - created: {self.created} - modified: {self.modified}" 
