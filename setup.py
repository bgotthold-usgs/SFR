from setuptools import setup
import glob

setup(
    name='sfr',
    version='0.0.1',
    description='Processing codes for building sfr features ',
    url='http://github.com/usgs-bcb/SFR',
    author='Ben Gotthold',
    author_email='bcb@usgs.gov',
    license='unlicense',
    packages=['urb','state'],
    data_files=[('urb', glob.glob('resources/*')),('state', glob.glob('resources/*'))],
    include_package_data=True,
    install_requires=[],
    zip_safe=False
)
