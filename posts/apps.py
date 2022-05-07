""" Post aplication module """
# importaciones --------------------------------------------
from django.apps import AppConfig

# Codigo ---------------------------------------------------
class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    """ Post aplication settings """
    name = 'posts'
    varbose_name = 'Posts'
