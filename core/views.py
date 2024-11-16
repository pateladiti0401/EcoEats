from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import csv
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import FoodItem, Notification
from .forms import CustomUserCreationForm, FoodItemForm, UserProfileForm
from .spoonacular_service import get_recipes_by_ingredients, get_recipe_details


# Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# Inventory Management
@login_required
def inventory(request):
    food_items = FoodItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.user = request.user
            food_item.save()
            messages.success(request, 'Item added successfully!')
            return redirect('inventory')
    else:
        form = FoodItemForm()
    return render(request, 'inventory.html', {'food_items': food_items, 'form': form})


# Update Food Item
@login_required
def update_food_item(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('inventory')
    else:
        form = FoodItemForm(instance=food_item)
    return render(request, 'inventory.html', {'form': form})


# Delete Food Item
@login_required
def delete_food_item(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk, user=request.user)
    food_item.delete()
    messages.success(request, 'Item deleted successfully!')
    return redirect('inventory')


# Profile Management
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


# Export Food Items to CSV
@login_required
def export_food_items_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="food_items.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Quantity', 'Expiration Date', 'Priority'])
    for item in FoodItem.objects.filter(user=request.user):
        writer.writerow([item.name, item.category, item.quantity, item.expiration_date, item.priority])
    return response


# Export Food Items to PDF
@login_required
def export_food_items_pdf(request):
    food_items = FoodItem.objects.filter(user=request.user)
    html = render_to_string('export_food_items.html', {'food_items': food_items})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="food_items.pdf"'
    HTML(string=html).write_pdf(response)
    return response
