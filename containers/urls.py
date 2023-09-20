from django.urls import path
from containers import views


urlpatterns = [
    path('containers/', views.ContainerList.as_view()),
    path('containers/<int:pk>/', views.ContainerDetail.as_view())
]