""" Middleware """
# importaciones ------------------------------------------------
# Django
from django.shortcuts import redirect
from django.urls import reverse

# Codigo -------------------------------------------------------
class ProfileCompletionMiddleware:
    """Perfil middleware.
        Asegúrese de que todos los usuarios que interactúan con la plataforma tienen su foto de perfil y biografía.
    """

    def __init__(self, get_response):
        #iniciacion del mideware
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)
        return response
