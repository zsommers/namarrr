"""
Django settings for django_namarrr project.

Demo settings

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from .base import *

INSTALLED_APPS += ('finalware',)

SITE_SUPERUSER_USERNAME = 'admin'
SITE_SUPERUSER_EMAIL = "zsommers@gmail.com"
SITE_SUPERUSER_PASSWORD = 'admin'
SITE_SUPERUSER_ID = '5432'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'namarrr',
    }
}
