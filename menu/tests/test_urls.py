'''Tests for Menu app URL configuration.'''

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import menu


class MenuURLTests(SimpleTestCase):
    '''Ensures menu URLs resolve to the correct views.'''

    def test_menu_url(self):
        '''Root URL should resolve to menu view.'''
        url = reverse('menu')
        self.assertEqual(resolve(url).func, menu)
