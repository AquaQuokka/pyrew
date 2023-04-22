from setuptools import setup, find_packages

setup(
    name='pyrew',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        "sys",
        "builtins",
        "importlib",
        "os",
        "contextlib",
        "logging",
        "asyncio",
        "time",
        "itertools",
        "threading",
        "re"
    ]
)