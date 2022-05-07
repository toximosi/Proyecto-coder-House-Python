"""User admin clases
    damos un aspecto mejor al administrador de django """
# importaciones --------------------------------------------------
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile #importamos nuestro modelo

# Code ------------------------------------------------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):#hereda del modelo Admin de django
    list_display = ('pk', 'user', 'first_name','last_name', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user',)#para que al pinchar el link nos lleve al detalle
    list_editable = ('phone_number', 'website', 'picture')#para poder editar los datos directamente en la tabla de admin

    search_fields = (#para la creación del buscador en el admin
        'user__email','user__username','user__first_name','user__last_name','phone_number'
    )

    list_filter = (#creacion de filtros en el lateral de admin
        'user__is_active', 'user__is_staff','created','modified',)

    fieldsets = ( #para cambiar el orden de los datos de admin en User
        ('Profile', {'fields': (('user', 'picture'),),}),
        ('Extra info', {'fields': (('website', 'phone_number'), ('biography'))}),
        ('Metadata', {'fields': (('created', 'modified'),),})
    )

    readonly_fields = ('created', 'modified',)#No se pueden editar

#para que los datos del perfil se incluyan en la crecación del USER
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

#para heredar del user
class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username','email','first_name','last_name','is_active','is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
