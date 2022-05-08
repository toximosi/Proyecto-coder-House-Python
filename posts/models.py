""" Posts models"""
#bibliografia:
    #https://docs.djangoproject.com/en/4.0/ref/models/fields/
# importaciones ------------------------------------------------------
#Django
from django.db import models
from django.contrib.auth.models import User



#modelos -------------------------------------------------------------
class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #? unique: para que no se repita el mail en la base de datos
    profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    print(profile)
    #? unique: para que no se repita el mail en la base de datos
    title = models.CharField(max_length=255, verbose_name="Título")
    photo = models.ImageField(upload_to='posts/photos', verbose_name="Foto")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    #?auto_now_add: que se cree automáticamente
    modified = models.DateTimeField(auto_now=True)
    #?auto_now: que se cree automáticamente

    def __str__(self):
           return '{} by @{}'.format(self.title, self.profile.username)
