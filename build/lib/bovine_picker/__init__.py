#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-02-18 21:38
# @Author  : lifangyi
# @File    : __init__.py.py
# @Software: PyCharm

from picker import Picker


if __name__ == '__main__':
    pc = Picker(locale='en')
    wd = pc.what_day('19991220')
    print(wd)
