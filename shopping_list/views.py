from django.shortcuts import render
from django.views import generic
from .models import ShoppingList
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

# Create your views here.

class Login(LoginView):
    template_name = 'shopping_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shopping-list')


class ShoppingLists(generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'


class ListItems(generic.DetailView):
    model = ShoppingList
    context_object_name = 'items'
    template_name = 'shopping_list/list_items.html'
    

class CreateList(generic.CreateView):
    model = ShoppingList
    fields = '__all__'
    success_url = reverse_lazy('shopping-list')


class UpdateList(generic.UpdateView):
    model = ShoppingList
    fields = '__all__'
    success_url = reverse_lazy('shopping-list')


class DeleteList(generic.DeleteView):
    model = ShoppingList
    context_object_name = 'list'
    success_url = reverse_lazy('shopping-list')