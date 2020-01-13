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
    packages=['urb', 'state', 'lcc','ecoIIIconus','ecoIIIak', 'resources'],
    data_files=[('resources', glob.glob('resources/*.py')),
                ('urb', glob.glob('resources/*.json') + glob.glob('urb/*.py')),
                ('state', glob.glob('resources/*.json') + glob.glob('state/*.py')),
                ('ecoIIIconus', glob.glob('resources/*.json') + glob.glob('ecoIIIconus/*.py')),
                ('ecoIIIak', glob.glob('resources/*.json') + glob.glob('ecoIIIak/*.py')),
                ('lcc', glob.glob('resources/*.json') + glob.glob('lcc/*.py'))],
    include_package_data=True,
    install_requires=[],
    zip_safe=False
)
