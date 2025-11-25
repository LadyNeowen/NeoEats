'''Tests for About app URL configuration.'''

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import (
    about,
    about_gallery,
    about_collaborations,
)


class AboutURLTests(SimpleTestCase):
    '''Ensures all URLs resolve to the appropriate views.'''

    def test_about_url(self):
        '''Root URL should resolve to about().'''
        self.assertEqual(resolve(reverse('about')).func, about)

    def test_about_gallery_url(self):
        '''/gallery/ should resolve to about_gallery().'''
        self.assertEqual(
            resolve(reverse('about_gallery')).func,
            about_gallery,
        )

    def test_about_collaborations_url(self):
        '''/collaborations-with-farmers/ should resolve to about_collaborations().'''
        self.assertEqual(
            resolve(reverse('about_collaborations')).func,
            about_collaborations,
        )
