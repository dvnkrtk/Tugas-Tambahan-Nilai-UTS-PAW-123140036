from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress',
]

setup(
    name='myclass_project',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = myclass_project:main',
        ],
    },
)
