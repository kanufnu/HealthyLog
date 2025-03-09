from django.contrib import admin
from .models import FoodItem, Meals


@admin.register(Meals)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'quantity', 'date')


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')



