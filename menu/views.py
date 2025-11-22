'''
Views for the Menu app.
'''

from django.shortcuts import render
from .models import MenuItem


def menu(request):
    '''
    Render the menu page.

    Retrieves:
        - Starters
        - Main courses
        - Desserts

    Template:
        menu/menu.html

    Context:
        starters (QuerySet[MenuItem])
        mains (QuerySet[MenuItem])
        desserts (QuerySet[MenuItem])
    '''
    starters = MenuItem.objects.filter(category='starter')
    mains = MenuItem.objects.filter(category='main')
    desserts = MenuItem.objects.filter(category='dessert')

    return render(
        request,
        'menu/menu.html',
        {
            'starters': starters,
            'mains': mains,
            'desserts': desserts,
        }
    )
