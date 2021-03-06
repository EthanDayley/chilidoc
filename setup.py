"""
The setup file for chilidoc
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name="chilidoc",
        version="1.0.0",
        description="Simple AsciiDoc style typesetting language converter",
        long_description=long_description,
        url="https://github.com/EthanDayley/chilidoc.git",
        author="Ethan Dayley",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3"
        ],
        keywords="markdown language typeset html converter",
        packages=["chilidoc"],
        zip_safe=False
    )
