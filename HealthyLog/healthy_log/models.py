from django.contrib.auth.models import User
from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=225)
    calories = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.name
    
    
class Meals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    
    
    def total_calories(self):
        return self.quantity * self.food_item.calories
    
    
    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"
    
    


