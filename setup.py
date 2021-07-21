"""This is the installation toolset for this project."""
from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='py_health_checker',
      version='0.1.0',
      author='w00fmeow',
      license = "BSD",
      keywords = "cli tool check up time health check web server",
      description='CLI tool to monitor uptime of a web server',
      long_description=long_description,
      install_requires=[
        'aiohttp>=3.7.4',
      ],
      packages=["py_health_checker"],
      entry_points={
      'console_scripts': [
          'py_health_checker = py_health_checker.__main__:main'
      ]
      })
