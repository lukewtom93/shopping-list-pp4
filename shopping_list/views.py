from django.shortcuts import render
from django.views import generic
from .models import ShoppingList
from django.urls import reverse_lazy

# Create your views here.

class ShoppingLists(generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'


class ListsItems(generic.DetailView):
    model = ShoppingList
    context_object_name = 'items'
    template_name = 'shopping_list/list_items.html'


class CreateList(generic.edit.CreateView):
    model = ShoppingList
    fields = '__all__'
    success_url = reverse_lazy('shopping-list')


class UpdateList(generic.edit.UpdateView):
    model = ShoppingList
    fields = '__all__'
    success_url = reverse_lazy('shopping-list')