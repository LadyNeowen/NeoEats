'''
Views for the Core app.
'''

from django.shortcuts import render


def home(request):
    '''
    Render the home page.
    '''
    return render(request, 'core/home.html')
