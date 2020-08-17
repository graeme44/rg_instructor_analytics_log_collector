"""Setup file."""

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="rg_instructor_analytics_log_collector",
    version="0.1",
    install_requires=[
        "setuptools",
    ],
    requires=[],
    packages=["rg_instructor_analytics_log_collector"],
    entry_points={"tutor.plugin.v0": ["myplugin = myplugin.plugin"]},
    description='Open edX log collector',
    long_description=README,
)
