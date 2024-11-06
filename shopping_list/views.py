from django.shortcuts import render
from django.views import generic
from .models import ShoppingList

# Create your views here.

class shopping_list(generic.ListView):
    model = ShoppingList
    context_object_name = 'items'


class list_items(generic.DetailView):
    model = ShoppingList