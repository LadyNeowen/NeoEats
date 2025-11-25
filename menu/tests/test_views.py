'''Tests for menu view.'''

from django.test import TestCase
from django.urls import reverse
from menu.models import MenuItem


class MenuViewTests(TestCase):
    '''Tests for the menu() view.'''

    def test_menu_view_renders(self):
        '''GET request should render template and include context keys.'''
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')
        self.assertIn('starters', response.context)
        self.assertIn('mains', response.context)
        self.assertIn('desserts', response.context)

    def test_menu_view_filters_categories(self):
        '''View should correctly group menu items into categories.'''
        MenuItem.objects.create(
            name='Soup',
            category='starter',
            price=8,
        )
        MenuItem.objects.create(
            name='Steak',
            category='main',
            price=20,
        )
        MenuItem.objects.create(
            name='Cake',
            category='dessert',
            price=7,
        )

        response = self.client.get(reverse('menu'))

        self.assertEqual(response.context['starters'].count(), 1)
        self.assertEqual(response.context['mains'].count(), 1)
        self.assertEqual(response.context['desserts'].count(), 1)
