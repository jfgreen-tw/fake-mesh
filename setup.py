#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Fake Mesh',
    version='0.1.0',
    description='A fake implementation of NHS Digital MESH, but one that should stand up to modest load',
    author='James Pickering',
    author_email='james.pickering@airelogic.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'fake_mesh': ['*.pem']},
    requires=[
        'cheroot (>=5.8.3)',
        'lmdb (>=0.93)',
        'six (>=1.10.0)',
        'werkzeug (>= 0.12.2)',
        'wrapt (>= 1.10.11)'
    ])
