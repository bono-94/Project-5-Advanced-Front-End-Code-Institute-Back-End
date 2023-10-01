from django.urls import path
from containers import views


urlpatterns = [
    path('containers/', views.ContainerList.as_view()),
    path('container/<int:pk>/', views.ContainerDetail.as_view()),
    path('containers/public/', views.PublicContainerList.as_view(), name='public-container-list'),
    path('containers/private/', views.PrivateContainerList.as_view(), name='private-container-list'),
]