# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='nbdemos',

    version='0.1.0',

    description='Functions and constants used by GBDX Notebooks demos.',
    long_description=long_description,

    author='Elizabeth Golden',
    author_email='elizabeth.golden@digitalglobe.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    packages=find_packages(exclude=['tests', 'docs', 'examples']),

    install_requires=requirements

)
