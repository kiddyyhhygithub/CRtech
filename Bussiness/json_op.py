#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 0018 下午 4:17
# @Author  : Richard
# @Site    : 
# @File    : json_op.py
# @email   : kiddyflash@163.com

import json
import time
from Bussiness.mongodb_op import DBHelper
def getjson():
    file_read = None
    with open(r'z:/1.txt','r') as f:
        file_read = json.loads( f.read() )
    # print(file_read)

    data = []
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #在线解析 https://c.runoob.com/front-end/53
    for fi in file_read['service']['data']['serviceData']['MeterReading']['datas']:
        # data.append({"name":fi['Reading']})
        data.append({"protocol":fi['protocol'],"id":fi['id'],"name": fi['Reading'],'time':fi['time'],"SysTime":timeStr})
        # print(fi['Reading'])
    print(data)
    db = DBHelper()
    db.insert_data(data)
    return file_read['service']['data']['serviceData']['MeterReading']['datas'][0]['time']


def obtain_body_json(body):
    '''

    :return:
    '''
    file_read = body
    data = []
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 在线解析 https://c.runoob.com/front-end/53
    for fi in file_read['service']['data']['serviceData']['MeterReading']['datas']:
        data.append({"protocol":fi['protocol'],"id":fi['id'],"name": fi['Reading'],'time':fi['time'],"SysTime":timeStr})
        # print(fi['Reading'])
    print(data)
    db = DBHelper()
    db.insert_data(data)
    return