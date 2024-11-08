from django.shortcuts import render
from django.views import generic
from .models import ShoppingList

# Create your views here.

class ShoppingLists(generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'


class ListsItems(generic.DetailView):
    model = ShoppingList
    context_object_name = 'items'
    template_name = 'shopping_list/list_items.html'