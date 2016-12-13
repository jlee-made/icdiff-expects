#!/usr/bin/env python

import ast
import codecs

from setuptools import setup


requirements = open('requirements.txt').read().splitlines()
requirements = ['icdiff-inprocess'] + [
    r for r in requirements if 'icdiff-inprocess' not in r]


def read_text(path):
    with codecs.open(path, "r", "utf-8") as fh:
        return fh.read()


def read_version(path):
    with open(path) as fh:
        for line in fh:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                continue
            elif line.startswith("from __future__ import"):
                continue
            else:
                if not line.startswith("__version__ = "):
                    raise Exception("Can't find __version__ line in " + path)
                break
        else:
            raise Exception("Can't find __version__ line in " + path)
        _, _, quoted = line.rstrip().partition("= ")
        return ast.literal_eval(quoted)


classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Testing",
]


setup(
    name="icdiff-expects",
    url='https://github.com/jlee-made/icdiff-expects',

    author='John Lee',
    author_email='john.lee@made.com',
    classifiers=classifiers,
    dependency_links=[
        "git+https://github.com/jlee-made/icdiff/tarball/master#egg=icdiff-inprocess"
    ],
    description="Readable coloured inline diffs from expects test assertions",
    license="BSD",
    long_description=read_text("README.md"),
    package_dir={"": "src"},
    platforms=["any"],
    py_modules=["icdiff_expects"],
    install_requires=requirements,
    test_suite="test_icdiff_expects",
    version=read_version("src/icdiff_expects.py"),
    zip_safe=True,
)
