from django.urls import path
from .views import register, inventory, update_food_item, delete_food_item, profile, export_food_items_csv, export_food_items_pdf

urlpatterns = [
    path('register/', register, name='register'),
    path('inventory/', inventory, name='inventory'),
    path('inventory/update/<int:pk>/', update_food_item, name='update_food_item'),
    path('inventory/delete/<int:pk>/', delete_food_item, name='delete_food_item'),
    path('profile/', profile, name='profile'),
    path('inventory/export/csv/', export_food_items_csv, name='export_food_items_csv'),
    path('inventory/export/pdf/', export_food_items_pdf, name='export_food_items_pdf'),
]
