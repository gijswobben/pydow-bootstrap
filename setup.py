import os
from setuptools import setup
from setuptools import find_packages
from pydow_bootstrap.version import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pydow_bootstrap",
    version=__version__,
    author="Gijs Wobben",
    author_email="gijswobben@gmail.com",
    description=("Bootstrap library for PyDow"),
    license="MIT",
    keywords="PyDow Bootstrap",
    url="https://github.com/gijswobben/pydow_bootstrap",
    packages=find_packages(),
    install_requires=["pydow"],
    tests_require=["pytest"],
    long_description_content_type="text/markdown",
    long_description=read("README.md"),
    classifiers=[
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
