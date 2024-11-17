from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('food_items/', views.food_item_list, name='food_item_list'),
    path('fooditem/update/<int:pk>/', views.FoodItemUpdateView.as_view(), name='food_item_update'),
    path('fooditem/delete/<int:pk>/', views.FoodItemDeleteView.as_view(), name='food_item_delete'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('recipes/', views.recipes, name='recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('export_food_items/', views.export_food_items, name='export_food_items'),
    path('user_history/', views.user_history, name='user_history'),
]
