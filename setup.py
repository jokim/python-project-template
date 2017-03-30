#!/bin/env python
# -*- encoding: utf8 -*-

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

def get_requirements(filename):
    """Read requirements from file"""
    with open(filename, 'r') as reqfile:
        for req_line in reqfile.readlines():
            req_line = req_line.strip()
            if req_line:
                yield req_line

setup(name='TODO',
      version='0.1',
      description="TODO",
      long_description=readme(),
      url="TODO.com",
      author="Joakim S. Hovlandsvåg",
      author_email="joakim.hovlandsvag@gmail.com",
      license="GPLv3",
      packages=['TODO'],
      install_requires=get_requirements('requirements.txt'),
      scripts=[
          # TODO
          ],
      include_package_data=True,
      #zip_safe=False,
      )

