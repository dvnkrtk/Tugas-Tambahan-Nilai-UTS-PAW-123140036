from setuptools import setup

requires = [
    'pyramid',
]

setup(
    name='myproject',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = myproject:main',
        ],
    },
)
