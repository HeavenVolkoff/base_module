#!/usr/bin/env python3

# find_namespace_packages requires setuptools>=40.1.0
from setuptools import setup, find_namespace_packages

setup(packages=find_namespace_packages("src"), package_dir={"": "src"})
