#!/usr/bin/env python
import sys
import glob
import os.path
from setuptools import setup, find_packages

MYDIR = os.path.dirname(os.path.abspath(__file__))

def find_pyfiles(localdir=''):
    path = os.path.join(MYDIR, localdir)
    pattern = os.path.join(path, '*.py')
    return glob.glob(pattern)

# find project packages
packages = find_packages(exclude=["test*"])
# find scripts
scripts = find_pyfiles('scripts')

setup(
    name = 's2a_api',
    version = '1.0',
    description = 'Ship2Anywhere API client library',
    package_dir = {'s2a_api': 's2a_api'},
    packages = packages,
    scripts = scripts,
    install_requires = [
        'argparse',
        #'beautifulsoup4==4.1.3',
        #'tornado==2.4',
    ],
)
