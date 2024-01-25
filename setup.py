# SPDX-FileCopyrightText: Nir Soffer <nirsof@gmail.com
# SPDX-License-Identifier: MIT

from setuptools import setup

import nohands

with open("README.md") as f:
    long_description = f.read()

setup(
    author="Nir Soffer",
    author_email="nirsof@gmail.com",
    description="A little library for effortless demos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    name="nohands",
    url="https://github.com/nirs/nohands",
    packages=["nohands"],
    install_requires=["PyYAML"],
    project_urls={
        "Source": "https://github.com/nirs/nohands",
        "Bug Tracker": "https://github.com/nirs/nohands/issues",
    },
    version=nohands.__version__,
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": ["nh=nohands.__main__:main"],
    },
)
