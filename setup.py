from setuptools import setup, find_packages

setup(
    name='pyrew',
    version='0.4.0',
    description='A Python library for writing shorter and more efficient Python code.',
    long_description="Welcome to Pyrew, a simple Python library for writing shorter and more efficient Python code. Simply install and import the module.",
    url="git+https://github.com/AquaQuokka/pyrew.git",
    author="AquaQuokka",
    license='BSD-3-Clause',
    py_modules=['pyrew'],
    scripts=['pyrew.py'],
    install_requires=[]
)