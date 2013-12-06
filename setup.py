# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages, Extension
try:
    import numpy as np
except ImportError:
    print "Please install numpy(1.6.0) first."
    print "pip install numpy==1.6.0"
    exit()

install_requires = [
    'numpy==1.6.0'
]

dependency_links = [
]

ext_modules = [
    Extension('cfuns', ['cfuns.c'])
]

if __name__ == '__main__':
    setup(name='srpp_travel',
          version='0.1',
          author=["Marek Piechula", "Michał Wesoły"],
          author_email=[],
          package_dir={'': 'src'},
          packages=find_packages('src'),
          install_requires=install_requires,
          dependency_links=dependency_links,
          include_dirs=[np.get_include()],
          ext_modules=ext_modules
          )
