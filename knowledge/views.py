from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to KNOWL3DG3 Containers!",
        "description": "This is an API for managing container information.",
        "endpoints": {
            "profiles": "/api/profiles/",
            "followers": "/api/followers/",
            "friends": "/api/friends/",   
            "containers": "/api/containers/",            
            "posts": "/api/posts/",        
            "comments": "/api/comments/",  
            "likes": "/api/likes/",        
            "favourites": "/api/favourites/", 
            "support": "/api/support/",
        }
    })
