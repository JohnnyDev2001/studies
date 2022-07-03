from django.urls import path
from core import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('index', views.index, name='index'),
]