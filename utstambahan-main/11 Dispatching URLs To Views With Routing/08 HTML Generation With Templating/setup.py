from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='mytemplate_project',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = mytemplate_project:main',
        ],
    },
)