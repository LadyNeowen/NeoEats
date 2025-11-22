'''
WSGI config for the neoeats_project project.

Exposes the WSGI application as a module-level variable `application`.
For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
'''

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neoeats_project.settings')

application = get_wsgi_application()
