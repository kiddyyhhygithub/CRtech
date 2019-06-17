#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 23:36
# @Author  : richie
# @Site    : 
# @File    : mongodb_op.py
# @Software: PyCharm
# @email   : kiddyflash@163.com

from pymongo import MongoClient
def get_info():
    conn = MongoClient('127.0.0.1',27017)
    db = conn.yh
    my_set = db.yh
    my_set.insert({'name':'richie'})

    return


