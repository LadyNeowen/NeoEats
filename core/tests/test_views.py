'''Tests for Core app views.'''

from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    '''Tests for the home view.'''

    def test_home_view_renders_template(self):
        '''Home view should return status 200 and render the correct template.'''
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
