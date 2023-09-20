from django.urls import path
from support import views


urlpatterns = [
    path('support/', views.SupportList.as_view()),
    path('support/<int:pk>/', views.SupportDetail.as_view())
]