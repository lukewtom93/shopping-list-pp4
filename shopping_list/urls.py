from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingLists.as_view(), name='shopping-list'),
    path('shopping-list/<int:pk>/', views.ListsItems.as_view(), name='list'),
    path('create-list', views.CreateList.as_view(), name='create-list'),
    path('update-list/<int:pk>/', views.UpdateList.as_view(), name='update-list'),
    path('delete-list/<int:pk>/', views.DeleteList.as_view(), name='delete-list'),
]
