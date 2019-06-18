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
def main():
    ##############插入多条记录##################
    # crdb = DBHelper('127.0.0.1',27017)
    # user_name1 = '胡玉3'
    # user_name2 = '胡玉4'
    # data = [{'name': user_name1},{'name': user_name2}]
    # crdb.insert_data(data)
    ##############################################


    ##############json解析#######################

    print(getjson())
    #############################################


    print("completed")
    return
if __name__ == '__main__':
    main()
