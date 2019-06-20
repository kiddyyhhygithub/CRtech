#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 22:31
# @Author  : richie
# @Site    : 
# @File    : Reflector.py
# @Software: PyCharm
# @email   : kiddyflash@163.com
class Refector:
    def __init__(self,value):
        self._value = value
        return
    @staticmethod
    def prt(self):
        print("ddd")
    @classmethod
    def prt1(self):
        print(self._value)
