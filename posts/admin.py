"""Posts model"""
#importaciones ----------------------------------------------
# Django
from django.contrib import admin
# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post en admin"""
    list_display = ( 
    #'user',
     'profile', 'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

