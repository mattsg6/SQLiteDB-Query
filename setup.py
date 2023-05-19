from setuptools import setup, find_packages
from querypackage import __version__

setup(
    name='query-sqlite',
    version=__version__,
    url='https://github.com/mattsg6/SQLiteDB-Query',
    author='Matthew Gilmore',
    author_email='thegilmores.matt@gmail.com',
    packages=find_packages(),
    license='GNU GENERAL PUBLIC LICENSE',
    
    entry_points={
        'console_scripts': [
            'query-sqlite=querypackage.main:cmd_start'
        ]
    }
)