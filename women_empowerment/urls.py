from django.urls import path
from . import views

urlpatterns = [
    path('', views.woman_list, name='woman_list'),
]
