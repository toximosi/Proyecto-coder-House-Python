from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photopost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #on_delete, cuando se borre el usuario se borren los post
    #? unique: para que no se repita el mail en la base de datos
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, verbose_name="Perfil")
    #? unique: para que no se repita el mail en la base de datos
    title = models.CharField(max_length=255, verbose_name="Título")
    photo = models.ImageField(upload_to='posts/photos', verbose_name="Foto")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    #?auto_now_add: que se cree automáticamente
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificación")
    #?auto_now: que se cree automáticamente