# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = __import__('googlytics').__version__

setup(
    name = 'django-googlytics',
    version = version,
    author = 'Riccardo Poggi',
    author_email = 'rik.poggi@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    url = 'https://github.com/rikpg/django-googlytics',
    license = 'BSD licence',
    description = 'Add google analytics snippet to your django templates.',
    long_description = open('README.md').read(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
    ),
)
