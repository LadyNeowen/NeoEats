'''Tests for the Core app configuration.'''

from django.test import SimpleTestCase
from django.apps import apps
from core.apps import CoreConfig


class CoreConfigTest(SimpleTestCase):
    '''Tests for CoreConfig class.'''

    def test_app_config_name(self):
        '''CoreConfig should have the correct app name.'''
        config = apps.get_app_config('core')
        self.assertEqual(config.name, 'core')
