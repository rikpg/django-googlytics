#!/bin/sh
export PYTHONPATH="./"
export DJANGO_SETTINGS_MODULE="tests.settings"

django-admin.py test $1 $2
