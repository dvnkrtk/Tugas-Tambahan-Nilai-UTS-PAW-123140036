from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyramid",
        "waitress",
        "pyramid_jinja2",
    ],
    entry_points={
        "paste.app_factory": [
            "main = myproject:main",
        ],
    },
)
