from django.urls import path
from content import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]
