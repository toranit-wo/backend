from django.urls import path
# from rest_framework import views

# from .views import ListPingponghit, DetailPingponghit
from apis import views

urlpatterns = [
    path('', views.pingponghit_list),
    path('<int:pk>/', views.pingponghit_detail)
]
