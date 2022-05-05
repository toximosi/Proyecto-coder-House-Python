"""User admin clases
    damos un aspecto mejor al administrador de django """
# importaciones --------------------------------------------------
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Code ------------------------------------------------------------
""" class ProfileAdmin (admin.ModelAdmin):
    # """
