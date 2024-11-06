from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_list.as_view(), name='shopping_list'),
    
]
