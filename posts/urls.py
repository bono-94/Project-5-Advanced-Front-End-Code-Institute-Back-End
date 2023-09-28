from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
     path('posts-by-containers/', views.PostListByContainers.as_view(), name='post-list-by-containers'),
    path('post/<int:pk>/', views.PostDetail.as_view())
]