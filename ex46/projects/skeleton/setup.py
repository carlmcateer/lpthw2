try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'descriprion': 'My Project',
    'author': 'Carl McAteer',
    'url': 'www.github.com/carlmcateer/lpthw2',
    'download_url': 'www.github.com/carlmcateer/lpthw2',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'LPTHW EX46'
]

setup(**config)
