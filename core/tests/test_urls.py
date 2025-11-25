'''Tests for Core app URL configuration.'''

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import home


class CoreURLTests(SimpleTestCase):
    '''Ensures Core app URLs map to the correct views.'''

    def test_home_url_resolves(self):
        '''Root URL should resolve to home view.'''
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
