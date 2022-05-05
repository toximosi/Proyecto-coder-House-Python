
""" USER model """
#bibliografia:
    #https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
    #https://docs.djangoproject.com/en/4.0/ref/models/fields/
#importaciones ---------------------------------------------------------
#django
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    """Profile model 
    modelo Proxy que extiende la base de datos con otra información"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True) 
    #? blank=True, que permite que se quede vacio
    website = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True )
    #upload_to: donde se guardarán las imágenes
    created = models.DateTimeField(auto_now_add=True)#fechas de creación 
    modified = models.DateTimeField(auto_now=True)#fecha de modificación 