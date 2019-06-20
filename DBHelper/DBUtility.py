#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 0020 下午 12:30
# @Author  : Richard
# @Site    : 
# @File    : DBUtility.py
# @email   : kiddyflash@163.com

from pymongo import MongoClient
import pymongo
class DBUtility():
    def __init__(self,url = '127.0.0.1',port = 27017,database = 'yanhua',collector = 'yh'):
        self._url = url
        self._port = port
        self._database = database
        self._collector = collector

    def insert_data(self,data):
        '''
        插入数据
        :param data:
        :return:
        '''
        result = False
        try:
            conn = MongoClient(host=self._url,port=self._port)
            db = conn[self._database]
            collector = db[self._collector]
            collector.insert(data)
            result = True
            pass
        except:
            pass

        return result




    def get_data(self,N=50,sort=True,sortId='_id'):
        '''
        获取数据库记录列表
        :param N:查询的记录数。默认50
        :param sort:是否正向排序，默认True为正向
        :return:返回数据列表
        '''
        resData = []
        seq = pymongo.DESCENDING
        if not sort:
            seq = pymongo.ASCENDING

        try:
            conn = MongoClient(host=self._url, port=self._port)
            db = conn[self._database]
            collector = db[self._collector]
            resData = collector.find().limit(N).sort(sortId,seq)
        except:
            pass

        return resData
