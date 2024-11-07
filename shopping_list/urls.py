from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_list.as_view(), name='shopping_list'),
    path('shopping_list/<int:pk>/', views.list_items.as_view(), name='list')
]
