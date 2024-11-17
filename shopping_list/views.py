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

# Login View
class Login(LoginView):
    template_name = 'shopping_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shopping-list')

# Register View
class Register(generic.FormView):
    template_name = 'shopping_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shopping-list')

    def form_valid(self, form):
        """
        Saves the form data to the database
        from a new user and loggs them in. 
        """
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        """
        Modifies the get function
        to redirect users to the main page
        and prevents authenticated users
        from accessing the Registration page.
        """
        if self.request.user.is_authenticated:
            return redirect('shopping-list')
        return super(Register, self).get(*args, **kwargs)

# Shopping list main page view
class ShoppingLists(LoginRequiredMixin, generic.ListView):
    model = ShoppingList
    context_object_name = 'lists'

    def get_context_data(self, **kwargs):
        """
        Ensures the content data passed to the
        template is user specific data
        """
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user = self.request.user)
        context['count'] = context['lists'].filter(complete=False)
        return context
    
# Create Item view
class CreateItem(LoginRequiredMixin, generic.CreateView):
    model = ShoppingList
    fields = ['title', 'quantity']
    success_url = reverse_lazy('shopping-list')

    def form_valid(self, form):
        """
        Automatically sets the user field
        to the logged in user.
        """
        form.instance.user = self.request.user
        return super(CreateItem, self).form_valid(form)

# Update Item view
class UpdateItem(LoginRequiredMixin, generic.UpdateView):
    model = ShoppingList
    fields = ['title', 'quantity']
    success_url = reverse_lazy('shopping-list')

# Delete Item View
class DeleteItem(LoginRequiredMixin, generic.DeleteView):
    model = ShoppingList
    context_object_name = 'list'
    success_url = reverse_lazy('shopping-list')

# Completed Item function
def UpdateComlpletedItem(request, item_id):
    """
    Retrives data to determine the item
    is completed and updates item accordingly.
    """
    data = json.loads(request.body)
    completed = data.get('completed', True)
    item = ShoppingList.objects.get(id=item_id)
    item.complete = completed
    item.save()
    return JsonResponse({'status': 'success', 'completed': item.complete})