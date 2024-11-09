from django.shortcuts import render
from django.views import generic
from .models import ShoppingList, Item
from django.urls import reverse_lazy

# Create your views here.

class ShoppingLists(generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'


class ListItems(generic.DetailView):
    model = ShoppingList
    context_object_name = 'items'
    template_name = 'shopping_list/list_items.html'


class Items(generic.DetailView):
    model = Item
    context_object_name = 'item'
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