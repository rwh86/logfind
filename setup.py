try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Logfind: search log files for strings',
    'author': 'Robert Hutton',
    'url': 'https://github.com/rwh86/logfind',
    'download_url': 'https://github.com/rwh86/logfind',
    'author_email': 'rwh@helms-deep.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lf'],
    'scripts': ['bin/logfind'],
    'name': 'logfind'
}

setup(**config)
