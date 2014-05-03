from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6ia4u+^1@yr1=i#ac$8wd^i2fyohwc#=mlq#je=b&kb*ih4n+8'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'namarrr',
    }
}

INSTALLED_APPS += ('debug_toolbar.apps.DebugToolbarConfig', )

ROOT_URLCONF = 'django_namarrr.urls'
