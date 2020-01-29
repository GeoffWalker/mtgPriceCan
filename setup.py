"""https://python-packaging.readthedocs.io/en/latest/minimal.html"""

from setuptools import setup

setup(name='mtgPriceCan',
      version='0.1',
      description='Scraper Canadian Prices for MTG Cards',
      url='https://github.com/GeoffWalker/mtgPriceCan',
      author='Geoff Walker',
      author_email='',
      license='MIT',
      packages=['mtgPriceCan'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['mtgPriceCan=mtgPriceCan.main:cli'],
    })