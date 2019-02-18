#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-02-18 21:38
# @Author  : lifangyi
# @File    : __init__.py.py
# @Software: PyCharm

from bovine_picker import picker


if __name__ == '__main__':
    pc = picker.Picker(locale='en')
    wd = pc.what_day('19991220')
    print(wd)
