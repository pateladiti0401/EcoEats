from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import FoodItemForm, RecipeForm
from .models import FoodItem, Recipe
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Register view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to a user-specific page, like a dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def dashboard(request):
    food_items = request.user.food_items.all()
    recipes = request.user.recipes.all()
    return render(request, 'dashboard.html', {'food_items': food_items, 'recipes': recipes})

@login_required(login_url='/login')
def food_item_list(request):
    food_items = request.user.food_items.all()
    return render(request, 'food_item_list.html', {'food_items': food_items})

@login_required(login_url='/login')
def add_food_item(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.user = request.user
            food_item.save()
            messages.success(request, 'Food Item added successfully!')
            return redirect('food_item_list')
    else:
        form = FoodItemForm()
    return render(request, 'add_food_item.html', {'form': form})

@login_required(login_url='/login')
def recipe_list(request):
    recipes = request.user.recipes.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required(login_url='/login')
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
