from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('', views.ShoppingLists.as_view(), name='shopping-list'),
    path('create-list', views.CreateList.as_view(), name='create-list'),
    path('update-list/<int:pk>/', views.UpdateList.as_view(), name='update-list'),
    path('update-completed-item/<int:item_id>/', views.UpdateComlpletedItem, name='update-completed-item'),
    path('delete-list/<int:pk>/', views.DeleteList.as_view(), name='delete-list'),
]
