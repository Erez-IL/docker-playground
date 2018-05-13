"""
Sample production-ready settings for patchwork project.

Most of these are commented out as they will be installation dependent.

Design based on:
    http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/
"""

from __future__ import absolute_import

import os

import django

from .base import *  # noqa

#
# Core settings
# https://docs.djangoproject.com/en/1.8/ref/settings/#core-settings
#

# Security
#
# You'll need to replace this to a random string. The following python code can
# be used to generate a secret key:
#
#      import string, random
#      chars = string.letters + string.digits + string.punctuation
#      print repr("".join([random.choice(chars) for i in range(0,50)]))

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Email
#
# Replace this with your own details

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Patchwork <patchwork@lists.osmocom.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
NOTIFICATION_FROM_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (
    ('Holger Freyther', 'holger@freyther.de'),
    ('Holger Freyther', 'holger+p@freyther.de'),
)

# Database
#
# If you're using a postgres database, connecting over a local unix-domain
# socket, then the following setting should work for you. Otherwise,
# see https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    },
}

#
# Static files settings
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-files
# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#manifeststaticfilesstorage
#

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/patchwork')

if django.VERSION >= (1, 7):
    STATICFILES_STORAGE = \
        'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']
