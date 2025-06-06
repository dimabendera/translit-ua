
import translitua

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='translitua',

    version=translitua.__version__,

    description='Official transliteration for Ukrainian and russian languages',
    long_description=long_description,

    url='https://github.com/dchaplinsky/translit-ua',

    author='dchaplinsky, enagorny',
    author_email='chaplinsky.dmitry@gmail.com, ideviantik@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        'Natural Language :: Ukrainian',
        'Natural Language :: Russian',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Text Processing',
    ],

    keywords='ukrainian transliteration',

    packages=find_packages(exclude=('tests',)),

    package_data={'': ['LICENSE']},
)
