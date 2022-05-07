"""User formularios"""
"""Bibliografia: 
    https://docs.djangoproject.com/en/4.0/topics/forms/
    https://docs.djangoproject.com/en/4.0/ref/forms/fields/
    https://docs.djangoproject.com/en/4.0/ref/forms/widgets/
    https://docs.djangoproject.com/en/4.0/ref/forms/validation/

"""
#importaciones ---------------------------------------------------------
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile

#code ---------------------------------------------------------
class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50, label="Nombre usuario")
    password = forms.CharField(max_length=70,widget=forms.PasswordInput(), label="Contraseña")
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(), label="Repite Contraseña") # widget para validar el password y para que no sea visible

    first_name = forms.CharField(min_length=2, max_length=50, label="Nombre")
    last_name = forms.CharField(min_length=2, max_length=50, label = "Apellidos")

    email = forms.CharField( min_length=6,max_length=70,widget=forms.EmailInput(), label="Email") #widget para que lo valide como mail

    def clean_username(self):
        """Username debe ser único"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()#exists(): si existe no debuelve un booleano
        if username_taken:#si existe el usuario valida y avisa
            raise forms.ValidationError('Este usuario ya existe')
        return username

    def clean(self):
        """Verificar el password """
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data

    def save(self):
        """Crear un perfil, lo guarda"""
        data = self.cleaned_data
        data.pop('password_confirmation')#sacamos este valor porque no necesitamos guardarlos
        user = User.objects.create_user(**data)#mandamos todo el diccioneario
        profile = Profile(user=user)
        profile.save()
