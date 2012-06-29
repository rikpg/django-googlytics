# -*- coding: utf-8 -*-
#
# Minimum amount of settings to run the googlytics test suite
#

# googlytics options are often overriden during tests
GOOGLE_ANALYTICS_KEY = 'U-XXX-X'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'myapp',
    'googlytics',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'googlytics.context_processors.googlytics',
)
