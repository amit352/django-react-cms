# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import cms

setup(
    name='django-react-cms',
    version='0.1.0',
    author=u'Leonardo Arroyo',
    author_email='contato@leonardoarroyo.com',
    packages=find_packages(),
    url='https://github.com/leonardoarroyo/django-react-cms',
    download_url = 'https://github.com/leonardoarroyo/django-react-cms/tarball/0.1.0',
    license='MIT',
    description='Manage and export react components to the client.',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    install_requires=INSTALL_REQUIREMENTS
)
