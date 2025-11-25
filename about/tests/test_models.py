'''Tests for the About app models.'''

from django.test import TestCase
from about.models import AboutPage, GalleryImage, CollaborationPage
from cloudinary.models import CloudinaryField


class AboutPageModelTest(TestCase):
    '''Tests for the AboutPage model.'''

    def test_str_method(self):
        '''__str__ should return a fixed label.'''
        page = AboutPage.objects.create(content='Test content')
        self.assertEqual(str(page), 'About Page Content')

    def test_default_title(self):
        '''Model should use default title when none is provided.'''
        page = AboutPage.objects.create(content='Example')
        self.assertEqual(page.title, 'About NeoEats')


class GalleryImageModelTest(TestCase):
    '''Tests for the GalleryImage model.'''

    def test_str_method(self):
        '''__str__ should return the title.'''
        img = GalleryImage.objects.create(title='Photo', image='dummy.jpg')
        self.assertEqual(str(img), 'Photo')

    def test_image_field_type(self):
        '''Image field should be a CloudinaryField.'''
        field = GalleryImage._meta.get_field('image')
        self.assertIsInstance(field, CloudinaryField)


class CollaborationPageModelTest(TestCase):
    '''Tests for the CollaborationPage model.'''

    def test_str_method(self):
        '''__str__ should return a fixed label.'''
        collab = CollaborationPage.objects.create(content='ABC')
        self.assertEqual(str(collab), 'Collaborations Page Content')

    def test_default_title(self):
        '''Default title should be applied.'''
        collab = CollaborationPage.objects.create(content='ABC')
        self.assertEqual(collab.title, 'Working With Our Farmers')
