"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='py_health_checker',
      version='0.1.0',
      author='w00fmeow',
      description='CLI tool to monitor uptime of a web server',
      long_description=long_description,
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'py_health_checker = py_health_checker.__main__:main'
          ]
      })
