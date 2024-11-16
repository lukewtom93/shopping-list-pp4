from django.shortcuts import render, redirect
from django.views import generic
from .models import ShoppingList
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class Login(LoginView):
    template_name = 'shopping_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shopping-list')


class Register(generic.FormView):
    template_name = 'shopping_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shopping-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('shopping-list')
        return super(Register, self).get(*args, **kwargs)


class ShoppingLists(LoginRequiredMixin, generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user = self.request.user)
        context['count'] = context['lists'].filter(complete=False)
        return context
    

class CreateList(LoginRequiredMixin, generic.CreateView):
    model = ShoppingList
    fields = ['title', 'quantity']
    success_url = reverse_lazy('shopping-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateList, self).form_valid(form)

class UpdateList(LoginRequiredMixin, generic.UpdateView):
    model = ShoppingList
    fields = ['title', 'quantity']
    success_url = reverse_lazy('shopping-list')


def UpdateComlpletedItem(request, item_id):
 
    data = json.loads(request.body)
    completed = data.get('completed', True)
    item = ShoppingList.objects.get(id=item_id)
    item.complete = completed
    item.save()
    return JsonResponse({'status': 'success', 'completed': item.complete})



class DeleteList(LoginRequiredMixin, generic.DeleteView):
    model = ShoppingList
    context_object_name = 'list'
    success_url = reverse_lazy('shopping-list')