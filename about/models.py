from django.db import models

# About Page Model
class AboutPage(models.Model):
    title = models.CharField(max_length=200, default='About NeoEats')
    content = models.TextField()

    def __str__(self):
        return 'About Page Content'

# Gallery Images Model
class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

# Collaborations Page
class CollaborationPage(models.Model):
    title = models.CharField(max_length=200, default='Working With Our Farmers')
    content = models.TextField()

    def __str__(self):
        return 'Collaborations Page Content'
