'''Tests ensuring the About app templates render expected content.'''

from django.test import TestCase
from django.urls import reverse
from about.models import AboutPage, CollaborationPage, GalleryImage


class TemplateRenderTests(TestCase):
    '''Tests for template rendering correctness.'''

    def test_about_template_displays_content(self):
        '''About page template should display title and content.'''
        AboutPage.objects.create(
            title='Our Story',
            content='Welcome to NeoEats',
        )
        response = self.client.get(reverse('about'))

        self.assertContains(response, 'Our Story')
        self.assertContains(response, 'Welcome to NeoEats')

    def test_collaboration_template_displays_title(self):
        '''Collaborations template should show content and title.'''
        CollaborationPage.objects.create(
            title='Farming Partners',
            content='We work with local farms.',
        )
        response = self.client.get(reverse('about_collaborations'))

        self.assertContains(response, 'Farming Partners')
        self.assertContains(response, 'We work with local farms.')

    def test_gallery_template_displays_images(self):
        '''Gallery template should display images with title and description.'''
        GalleryImage.objects.create(
            title='Dish 1',
            description='Tasty food',
            image='dummy.jpg',
        )
        response = self.client.get(reverse('about_gallery'))

        self.assertContains(response, 'Dish 1')
        self.assertContains(response, 'Tasty food')
