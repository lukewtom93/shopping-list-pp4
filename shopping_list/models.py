from django.db import models
from django.contrib.auth.models import User

# Main model for shopping list
class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.quantity}"