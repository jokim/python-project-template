#!/bin/env python
# -*- encoding: utf8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


def get_readme():
    with open(path.join(here, 'README.rst'), 'r') as f:
        return f.read()


def get_requirements(filename):
    """Read requirements from file"""
    with open(path.join(here, filename), 'r') as reqfile:
        for req_line in reqfile.readlines():
            req_line = req_line.strip()
            if req_line:
                yield req_line


setup(name='TODO',
      version='0.1',
      description="TODO",
      long_description=get_readme(),
      long_description_content_type='text/markdown',
      # url="TODO.com",
      author="Joakim S. Hovlandsvåg",
      author_email="joakim.hovlandsvag@gmail.com",
      license="GPLv3+",
      packages=find_packages(),
      install_requires=list(get_requirements('requirements.txt')),
      scripts=[
          # TODO
          ],
      include_package_data=True,
      python_requires='>=2.6, <3',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Environment :: Console',
          'Operating System :: POSIX :: Linux',
      ],
      keywords='TODO',
      )
