""" Posts models"""
#bibliografia:
    #https://docs.djangoproject.com/en/4.0/ref/models/fields/
# importaciones ------------------------------------------------------
#Djngo
from django.db import models


#modelos -------------------------------------------------------------
class User(models.Model):
    email = models.EmailField(unique=True)
    #? unique: para que no se repita el mail en la base de datos
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)#biografia
    #? blank: acepta espacios vacios
    birthdate = models.DateField(blank=True, null=True)
    #?null: permite nulos
    created = models.DateTimeField(auto_now_add=True)#fecha de creacion
    #?auto_now_add: que se cree automáticamente
    modified = models.DateTimeField(auto_now=True)#fecha de modificacion

    is_admin = models.BooleanField(default=False) #filtro, para saber si es administrador
    #? deafult: valor por defecto
    def __str__(self):
        return f"email: {self.email} - password: {self.password} - first_name: {self.first_name} - last_name: {self.last_name} - bio: {self.bio} - birthdate: {self.birthdate} - created: {self.created} - modified: {self.modified} - is_admin: {self.is_admin}"
