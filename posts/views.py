""" Visatas """
# importaciones -----------------------------------------------------------------
#Django
from django.http import HttpResponse

# code -----------------------------------------------------------------
def postsList(requests):
    """lists existing posts"""
    posts = [1,2,4]
    return HttpResponse(str(posts))
