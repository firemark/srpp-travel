# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages, Extension
try:
    import numpy as np
except ImportError:
    print "Please install numpy(1.6.0) first."
    print "pip install numpy==1.6.0"
    exit()

install_requires = [
    'numpy==1.6.0',
    #'processing==0.52',
    'matplotlib==1.3.1'
]

ext_modules = [
    Extension('srpp_travel.cfuns', ['srpp_travel/cfuns.c'])
]

if __name__ == '__main__':
    setup(name='srpp-travel',
          version='0.1',
          author=["Marek Piechula", "Michał Wesoły"],
          author_email=[],
          packages=find_packages(),
          install_requires=install_requires,
          include_dirs=[np.get_include()],
          ext_modules=ext_modules
          )
