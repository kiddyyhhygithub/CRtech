#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 23:36
# @Author  : richie
# @Site    : 
# @File    : mongodb_op.py
# @Software: PyCharm
# @email   : kiddyflash@163.com

from pymongo import MongoClient
import pymongo
from Classes.Meter import Meter
class DBHelper():

    def __init__(self,_url_str='127.0.0.1',_port=27017):
        self.url_str = _url_str
        self.port = _port

    def get_info(self):
        # conn = MongoClient('127.0.0.1',27017)
        # db = conn.yh
        # my_set = db.yh
        # my_set.insert({'name':'richie'})
        conn = MongoClient("127.0.0.1",port=27017)
        db = conn.yanhua
        collection = db.yh
        data = {'name':'huyu12','name':'zhangsan'}
        collection.insert(data)
        print("end")
        return


    def insert_data(self,_data):
        '''
        插入数据
        :param data:一条或者多条字典数据
        :return:
        '''
        conn = MongoClient(self.url_str,self.port)
        db = conn.yanhua
        collection = db.yh

        # user_name = '胡玉'
        # data = {'name':'胡玉'}
        collection.insert(_data)
        return

    def show_data(self,N = 50,sort = pymongo.DESCENDING):
        '''
        获取历史数据
        :param N:
        :param sort:
        :return:返回实体类列表
        '''
        conn = MongoClient(self.url_str, self.port)
        db = conn.yanhua
        collection = db.yh
        data = collection.find().limit(N).sort('_id',sort)
        obj = []
        for d in data:
            str = '%s--%s--%s--%s--%s'%(d['protocol'],d['id'],d['name'],d['time'],d['SysTime'])
            # meter = Meter()
            # meter.Protocol = d['protocol']
            # meter.MeterID = d['id']
            # meter.Time = d['time']
            # meter.SysTime = d['SysTime']
            # obj.append(meter)
            print(str)
        return obj



