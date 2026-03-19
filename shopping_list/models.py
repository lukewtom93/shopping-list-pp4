from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    # Main model for shopping list
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.quantity}"
