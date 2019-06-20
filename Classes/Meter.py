#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 0:48
# @Author  : richie
# @Site    : 
# @File    : Meter.py
# @Software: PyCharm
# @email   : kiddyflash@163.com

class Meter(object):

    # def __init__(self,_reading):
    #     self.reading = _reading
    #     return
    def __init__(self):
        # self.reading = _reading
        return
    @property
    def Protocol(self):
        return self._protocol
    @Protocol.setter
    def Protocol(self,value):
        self._protocol = value


    @property
    def Time(self):
        return self._time
    @Time.setter
    def Time(self,value):
        self._time = value

    @property
    def Reading(self):
        '''读数'''
        return self._reading

    @Reading.setter
    def Reading(self,value):
        self._reading = value

    @property
    def SysTime(self):
        return self._systime
    @SysTime.setter
    def SysTime(self,value):
        self._systime  = value

    @property
    def MeterID(self):
        return self._meterid
    @MeterID.setter
    def MeterID(self,value):
        self._meterid = value