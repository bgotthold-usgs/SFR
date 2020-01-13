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
    packages=['urb', 'state', 'lcc','county', 'resources'],
    data_files=[('resources', glob.glob('resources/*.py')),
                ('urb', glob.glob('resources/*.json') + glob.glob('urb/*.py')),
                ('state', glob.glob('resources/*.json') + glob.glob('state/*.py')),
                ('lcc', glob.glob('resources/*.json') + glob.glob('lcc/*.py')),
                ('county',glob.glob('resources/*.json') + glob.glob('county/*.py'))],
    include_package_data=True,
    install_requires=[],
    zip_safe=False
)
