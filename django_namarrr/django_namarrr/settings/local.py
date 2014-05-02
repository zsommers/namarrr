from .base import *
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

# MIDDLEWARE_CLASSES += ('debug_toobar.middleware.DebugToobarMiddleware', )

# DEBUG_TOOLBAR_PATCH_SETTINGS = False
