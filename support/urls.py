from django.urls import path
from support import views


urlpatterns = [
    path('support/', views.SupportList.as_view()),
]