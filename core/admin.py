# core/admin.py
from django.contrib import admin
from .models import Profile, FoodItem, Recipe  # Import your models

# Register your models here
admin.site.register(FoodItem)
admin.site.register(Recipe)
admin.site.register(Profile)