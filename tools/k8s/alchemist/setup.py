import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
PATH_VERSION = os.path.join(HERE, 'alchemist', '__version__.py')

ABOUT = {}
with open(PATH_VERSION, mode='r', encoding='utf-8') as f:
    exec(f.read(), ABOUT)


setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    packages=find_packages(
        exclude=['*.tests']
    ),
    entry_points={
        'console_scripts': ['abracadabra=alchemist.app:run']
    },
    install_requires=[
        'PyYaml==5.4',
        'flask==1.0.2',
    ],
    extras_require={
        'dev': [
            'pytest==3.6.4',
            'pytest-cov==2.6.0'
        ]
    },
    setup_requires=[
        'pytest-runner'
    ]
)
