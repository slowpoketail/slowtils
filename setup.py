#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="slowtils",
    description="slowpoke's python utilities",
    author="slowpoke",
    author_email="mail+python@slowpoke.io",
    url="http://github.com/proxypoke/slowtils",
    version="0.1",
    packages=[
        "slowtils",
        "slowtils.func",
    ],
    py_modules = [
        "slowtils.file",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    license='ANTI-LICENSE',
)
