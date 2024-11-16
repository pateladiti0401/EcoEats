from django.urls import path
from . import views


urlpatterns = [
      path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('food_items/', views.food_item_list, name='food_item_list'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]
