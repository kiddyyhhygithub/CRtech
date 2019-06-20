#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 0020 上午 10:08
# @Author  : Richard
# @Site    : 
# @File    : Student.py
# @email   : kiddyflash@163.com

class Student(object):

    @property
    def birth(self):
        '''可读可写'''
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        '''只读'''
        return 2014 - self._birth



