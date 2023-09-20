from django.urls import path
from favourites import views

urlpatterns = [
    path('support/', views.FavouriteList.as_view()),
    path('support/<int:pk>/', views.FavouriteDetail.as_view())
]