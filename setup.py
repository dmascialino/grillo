#!/usr/bin/env python3
import os.path
from setuptools import setup, find_packages


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("grillo", "version.py")) as fp:
    exec(fp.read(), version)


setup(
    name="Grillo",
    version=version["__version__"],
    author="Juan Pedro Fisanotti",
    author_email="fisadev@gmail.com",
    description=("A small tool to easily send data (files, clipboard) between computers with 0 "
                 "config, just using audio and mic."),
    long_description=open("README.md").read(),
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/fisadev/grillo",
    entry_points = {
        'console_scripts': ['grillo=grillo.grillo:main'],
    },
    install_requires=[
        "chirpsdk",
        "pyperclip",
        "fire",
        "termcolor",
        "trailets",  # dependency of chirp, but missing in their requirements
    ],
)
