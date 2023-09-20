from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to KNOWL3DG3 Containers!",
        "description": "This is an API for managing container information.",
        "endpoints": {
            "profiles": "/profiles/",
            "followers": "/followers/",
            "containers": "/containers/",            
            "posts": "/posts/",        
            "comments": "/comments/",  
            "likes": "/likes/",        
            "favourites": "/favourites/", 
            "support": "/support/",
        }
    })
