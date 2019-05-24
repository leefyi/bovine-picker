#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-02-18 21:42
# @Author  : lifangyi
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name='bovine_picker',
    version='0.0.6',
    keywords='bovine-birthday test pypi',
    description='a library for test pypi distribution process',
    license='MIT License',
    url='https://github.com/leefyi/bovine_picker',
    author='lifangyi',
    author_email='leefyi@126.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[],
)
