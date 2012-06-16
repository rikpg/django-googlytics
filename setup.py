# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-googlytics',
    version='0.1',
    author=u'Riccardo Poggi',
    author_email='rik.poggi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/rikpg/django-googlytics',
    license='BSD licence, see LICENCE file',
    description='Add google analytics snippet to your django templates.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
