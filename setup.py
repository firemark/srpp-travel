# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    #'numpy==1.8.0'
]

dependency_links = [
]

if __name__ == '__main__':
    setup(name='srpp-travel',
          version='0.1',
          author=["Marek Piechula", "Michał Wesoły"],
          author_email=[],
          packages=find_packages(),
          install_requires=install_requires,
          dependency_links=dependency_links,
          )
