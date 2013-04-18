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
    name = 's2a_api_client',
    version = '1.0',
    description = 'Ship2Anywhere API client library',
    package_dir = {'s2a_api_client': 's2a_api_client'},
    packages = packages,
    scripts = scripts,
    install_requires = [
        'argparse', 
        'requests==1.1.0',
    ],
)
