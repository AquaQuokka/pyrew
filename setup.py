from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pyrew',
    version='0.12.0',
    description='A Python library for writing shorter and more efficient Python code.',
    long_description=long_description,
    url="https://github.com/AquaQuokka/pyrew",
    author="AquaQuokka",
    license='BSD-3-Clause',
    py_modules=['pyrew'],
    scripts=['pyrew.py'],
    install_requires=["humanize"],
)
