from django.db import models
from menu.models import Food

class CartItem(models.Model):
    food = models.ForeignKey(Food , on_delete = models.CASCADE , related_name = 'cart_items')
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity}x {self.food.name} in cart"
