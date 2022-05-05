""" Posts models"""
# importaciones ------------------------------------------------------
#Djngo
from django.db import models


#modelos -------------------------------------------------------------
class Post(models.Model):
    titulo = models.CharField()
    autor = models.CharField()
    fecha = models.DateField()
    
