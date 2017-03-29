from setuptools import setup

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ahg48',
    description='AHG 48',
    long_description=long_description,
    version='0.1.4',
    url='https://github.com/rch850/ahg48',
    author='rch850',
    author_email='rich850@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
    ],
    keywords='sample',
    packages=['ahg48'],
    entry_points={
        'console_scripts': [
            'encrypt=ahg48.main:run'
        ]
    }
)
