#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-02-18 15:41:36

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-qiniu-app",
    version="1.1.0",
    author="Xiang Wang",
    author_email="ramwin@qq.com",
    description="django的七牛app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramwin/django-qiniu-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "django",
        "djangorestframework",
        "qiniu",
    ],
)
