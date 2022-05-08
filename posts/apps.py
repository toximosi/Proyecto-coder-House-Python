""" Post aplication module """
from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    """ Post aplication settings """
    name = 'posts'
    varbose_name = 'Posts'
