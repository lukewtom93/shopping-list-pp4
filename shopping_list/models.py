from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShoppingList(models.Model):
    title = models.CharField(max_length=50, default='Shopping list')