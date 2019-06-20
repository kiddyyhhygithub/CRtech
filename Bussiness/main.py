#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 23:37
# @Author  : richie
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @email   : kiddyflash@163.com

from Bussiness.mongodb_op import DBHelper
from Bussiness.json_op import getjson
from Classes.Reading import Reading
from Bussiness.mongodb_op import DBHelper
from Classes.Meter import Meter
from DBHelper.DBUtility import DBUtility
import json
from pymongo import MongoClient
import pymongo
import time
def main():
    ##############插入多条记录##################
    # crdb = DBHelper('127.0.0.1',27017)
    # user_name1 = '胡玉3'
    # user_name2 = '胡玉4'
    # data = [{'name': user_name1},{'name': user_name2}]
    # crdb.insert_data(data)
    ##############################################


    ##############json解析#######################

    # print(getjson())
    #############################################


    ###############显示数据########################

    # db = DBHelper('127.0.0.1',27017)
    # db.show_data()
    #############################################

    # dict = {'Name': 'Runoob'}
    #
    # print("dict['Name']: ", dict['Name'])
    # print("completed")
######################################################
    # meter = Meter()
    # meter.Reading = "332"
    #
    # print(meter.Reading)


  ####################自定义属性########################
    # from Classes.Student import Student
    # student = Student()
    # student.birth = 1990
    # print(student.age)
    #
    # meter_class = Reading()
    # meter_class.name = 1223
    # print(meter_class.name)
    ########################################################
    # db = DBHelper()
    # data = db.show_data()
    # for d in data:
    #     print(d.Protocol)
    # return

    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    ####################################################
    # data_str = ''
    # data = []
    # with open(r'z:/1.txt','r') as f:
    #     data_str = f.read()
    # data_obj = json.loads(data_str)
    # for fi in data_obj['services'][0]['data']['serviceData']['MeterReading']['datas']:
    #     data.append({"protocol":fi['protocol'],"id":fi['id'],"name": fi['Reading'],'time':fi['time'],"SysTime":timeStr})
    #
    #
    # dbU = dbutility()
    # # data = [{'name':'yanhua'},{'name':'huyu'}]
    # print( dbU.insert_data(data) )
    # # print(data)

    ####################################################
    # conn = MongoClient(host='127.0.0.1',port=27017)
    # db = conn['yanhua']
    # colloect = db['yh']
    # data = colloect.find().limit(50).sort('_id',pymongo.DESCENDING)
    # for d in data:
    #     print(d['_id'])
#############################################
    # db = DBHelper()
    # data = db.show_data()
    # for d in data:
    #     print(d['protocol'])
    ##########################################
    db = DBUtility()
    data = db.get_data()
    for d in data:
        print(d['protocol'])


    seq = pymongo.DESCENDING


    # try:
    #     N = 50
    #     conn = MongoClient('127.0.0.1',27017)
    #     db = conn['yanhua']
    #     collector = db['yh']
    #     resData = collector.find().sort({'_id'})
    #     for d in resData:
    #         print(d['protocol'])
    # except:
    #     pass

    pass
if __name__ == '__main__':
    main()
