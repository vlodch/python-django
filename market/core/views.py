from django.shortcuts import render, redirect
from django.urls import reverse

from item.models import Category, Item

from .forms import SignupForm

# def index(request):
#     items = Item.objects.filter(is_sold=False)[0:6]
#     categories = Category.objects.all()

#     # Define the correct path to the dashboard template
#     dashboard_link = reverse('dashboard:index')  # Get the URL using the name of the URL pattern

#     return render(request, 'core/index.html', {
#         'categories': categories,
#         'items': items,
#         'dashboard_link': dashboard_link,  # Pass the dashboard link to the template
#     })

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'dashboard': 'dashboard:index',  # Pass the correct path to the dashboard
        'inbox': '/inbox/',
    })

def contact(request):
    return render(request, 'core/contact.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
