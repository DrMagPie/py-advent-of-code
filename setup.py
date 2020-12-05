from setuptools import setup

setup(
    name='AdventOfCode',
    packages=['pyaoc'],
    version='0.0.0',
    description='Function wrapper for Advent of Code',
    license="MIT",
    long_description='Wrapper That gets Advent of Code challenge input and submits returned data',
    url='https://github.com/DrMagPie/AdventOfCode',
    author='Dmitrijs Sorokins',
    install_requires=[
        'appdirs',
        'requests',
    ],
    python_requires='>=3.6'
)