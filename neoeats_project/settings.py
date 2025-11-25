"""
Django settings for the neoeats_project project.
"""

import os
import sys
from pathlib import Path

import dj_database_url



# Load environment variables (local development)
if os.path.isfile("env.py"):
    import env  # noqa: F401

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "neoeats.herokuapp.com",
    "neoeats-62e4965fe040.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://neoeats.herokuapp.com",
    "https://neoeats-62e4965fe040.herokuapp.com",
]

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Cloudinary
    "cloudinary_storage",
    "cloudinary",

    # Local apps
    "core",
    "menu",
    "about",
    "booking",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "neoeats_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "neoeats_project.wsgi.application"

# Database
DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Use SQLite during tests
if "test" in sys.argv:
    DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        )
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

if 'test' in sys.argv:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    
    
WHITENOISE_USE_FINDERS = True

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Cloudinary
DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)

# Security headers
X_FRAME_OPTIONS = "SAMEORIGIN"

# Default primary key field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "ERROR"},
}

# Email backend
if DEBUG:
    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
    )
