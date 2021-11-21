#!/usr/bin/python

# from distutils.core import setup
import os, re
import codecs
from setuptools import setup, find_packages, find_namespace_packages

def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
      name='version-build-demo',
      version=find_version("__init__.py"),
      description='demo script',
      author='everything developers',
      maintainer='witchc',
      license='MIT',
      package_dir={"project_a":""},
      packages = find_packages("../"),
      include_package_data=True,
      zip_safe=False, 
      install_requires=[
        'Click',
      ],entry_points={
        'console_scripts': [
            'version-build-demo = main:cli',
        ],
    },
    python_requires='>=3'
)