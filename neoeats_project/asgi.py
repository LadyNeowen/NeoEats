"""
ASGI config for the neoeats_project project.

Exposes the ASGI callable as a module-level variable named `application`.
For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neoeats_project.settings")

application = get_asgi_application()
