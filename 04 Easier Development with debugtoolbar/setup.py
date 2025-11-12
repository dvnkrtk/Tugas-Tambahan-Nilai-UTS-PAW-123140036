# setup.py
from setuptools import setup, find_packages

requires = [
    "pyramid",
    "waitress",
    "pyramid_jinja2",
    "pyramid_debugtoolbar",
]

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = myproject:main",
        ],
    },
)
