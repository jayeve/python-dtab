import os
from setuptools import setup, find_packages


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


README = local_file('README.md')


setup(
    name='pydtab',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',
    description='Library for parsing Finagle delegation tables (dtabs)',
    long_description=open(README).read(),
    url='https://github.com/justinvenus/python-dtab',
    author='Justin Venus',
    author_email='infra@strava.com',
    license='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
    install_requires=[
        'attrs',
    ],
    extras_require={
        'dev': [
            'flake8',
            'pytest',
        ],
    },
)
