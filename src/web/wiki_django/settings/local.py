# -*- coding: utf-8 -*-
"""
Django development settings for wiki_django project.
"""
from . import *  # noqa


# Debug
DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# Application definition
INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wiki_django',
        'USER':  'wiki_django',
        'HOST': 'postgresql',
        'PASSWORD': 'password',
        'PÓRT': 5432
    }
}


# Debug toolbar
INTERNAL_IPS = ('172.17.0.1',)
