from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('', views.ShoppingLists.as_view(), name='shopping-list'),
    path('create-item', views.CreateItem.as_view(), name='create-item'),
    path('update-item/<int:pk>/', views.UpdateItem.as_view(),
         name='update-item'),
    path('update-completed-item/<int:item_id>/', views.UpdateComlpletedItem,
         name='update-completed-item'),
    path('delete-item/<int:pk>/', views.DeleteItem.as_view(),
         name='delete-item'),
]
