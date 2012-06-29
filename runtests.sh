#!/bin/sh
export PYTHONPATH="./:./tests/"
export DJANGO_SETTINGS_MODULE="settings"

django-admin.py test $1 $2 myapp
