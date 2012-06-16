=================
Django-Googlytics
=================

A Django application for easily adding the google analytics snippet code to your templates.

The goole analytics code will be conditionally included in the template if the setted key is more than just an empty string.

Note: This app is a most simple implementation of the ideas expressed in these [StackOverflow answers](http://stackoverflow.com/questions/629696/deploying-google-analytics-with-django)


Installation
------------

Add the app to `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'googlytics',
        ...
    )

And add its context processor to `TEMPLATE_CONTEXT_PROCESSORS`:

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'googlytics.context_processors.googlytics',
    )

Then in your development settings add:

    GOOGLE_ANALYTICS_KEY = ''

And in your production settings add the real google analytics key:

    GOOGLE_ANALYTICS_KEY = 'UA-XXX-X'


Usage
-----

Just include googlytics code in your template with:

    {{ googlytics_code }}

That will show your google analytics code if there's an actual setted key (instad of an empty string).
