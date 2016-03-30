try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Generic utility for packaging projects',
    'author': 'Jeff Bowman',
    'version': '0.1',
    'url': 'http://www.google.com',
    'install_requires': ['nose', 'pyyaml'],
    'packages': ['packager'],
    'scripts': [],
    'name': 'packager'
}

setup(**config)
