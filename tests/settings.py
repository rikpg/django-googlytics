# -*- coding: utf-8 -*-
#
# Test settings
#

# Googlytics options set at runtime during tests
"""
GOOGLE_ANALYTICS_KEY = 'U-XXX-X'
GOOGLE_ANALYTICS_IGNORE_ADMIN = True
"""

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'googlytics.context_processors.googlytics',
)

INSTALLED_APPS = (
    'tests.myapp',
    'googlytics',
)
