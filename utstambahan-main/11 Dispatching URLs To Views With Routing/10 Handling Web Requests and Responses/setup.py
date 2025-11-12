from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
]

setup(
    name='myrequest_project',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = myrequest_project:main',
        ],
    },
)
