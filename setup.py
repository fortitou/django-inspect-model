# -*- coding: utf-8 -*-
from distutils.core import setup
from os.path import abspath, dirname, join
from setuptools import find_packages


def read_relative_file(filename):
    """Returns contents of the given file, whose path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


setup(
    name='django-inspect-model',
    version=read_relative_file('VERSION').strip(),
    author=u'Mathieu agopian',
    author_email='mathieu.agopian@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/magopian/django-inspect-model',
    license='BSD license, see LICENSE file',
    description='Model inspection for Django',
    long_description=open('README.rst').read(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
