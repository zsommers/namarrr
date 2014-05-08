"""
Django settings for django_namarrr project.

Local developer settings

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!

DEBUG = False
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'namarrr',
    }
}
