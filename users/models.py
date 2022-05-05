from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    nombre =  models.CharField()
    apellido = models.CharField()
    seudonimo = models.CharField()
    avatar = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField()

    """ class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk}) """
)