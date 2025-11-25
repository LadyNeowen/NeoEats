'''Tests for Menu app admin configuration.'''

from django.test import TestCase
from django.contrib import admin
from menu.models import MenuItem


class MenuAdminTests(TestCase):
    '''Tests ensuring MenuItem is registered in admin.'''

    def test_menu_item_registered(self):
        '''MenuItem should be registered with admin site.'''
        self.assertIn(MenuItem, admin.site._registry)
