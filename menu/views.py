from django.shortcuts import render
from .models import MenuItem

def menu(request):
    starters = MenuItem.objects.filter(category='starter')
    mains = MenuItem.objects.filter(category='main')
    desserts = MenuItem.objects.filter(category='dessert')

    return render(request, "menu/menu.html", {
        "starters": starters,
        "mains": mains,
        "desserts": desserts,
    })
