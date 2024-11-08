from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingLists.as_view(), name='shopping_list'),
    path('shopping_list/<int:pk>/', views.ListsItems.as_view(), name='list')
]
