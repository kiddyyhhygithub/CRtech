# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
import time
from pymongo import MongoClient
# Create your views here.
# from Bussiness.json_op import obtain_body_json
def data_his(request):
    # timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # body_req = request.body
    # body_req = request.body + timeStr +  '\r\n'
    # with open('./logs/testlog.txt','a+') as f:
    #     f.write(body_req)
    # json_obj = json.loads(body)
    # obtain_body_json(json_obj)
    # try:
    #     json_obj = json.loads(body)
    #
    #     obtain_body_json(json_obj)
    # except:
    #     pass
    # return HttpResponse(json_obj)
    # return HttpResponse(json_obj['name'])
    # with open('log.txt',"a+") as f:
    #     f.write(body)
    # return HttpResponse(body_req)
    bodyStr = request.body.decode('utf-8')
    # bodyStr = request.body


    # write_value = "%s%s" % (bodyStr, '\n')
    # with open('./logs/testlog.txt', 'a+') as f:
    #     f.write(write_value)



    # try:
    #     # json_obj = json.loads(body)
    #     #
    #     # obtain_body_json(json_obj)
    #     json_obj = json.loads(body)
    #     conn = MongoClient('127.0.0.1',27017)
    #     db = conn.yanhua
    #     my_set = db.yh
    #
    #     datas = []
    #     # for fi in json_obj['service'][0]['data']['serviceData']['MeterReading']['datas']:
    #     #     # data.append({"protocol":fi['protocol'],"id":fi['id'],"name": fi['Reading'],'time':fi['time'],"SysTime":timeStr})
    #     #     datas.append({"protocol":"yhhy"})
    #     # my_set.insert(data)
    #     datas.append({"protocol":"yhhy"})
    #     my_set.insert(datas)
    #
    #
    # except:
    #     pass
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data = []
    obj = json.loads(bodyStr)
    Reading = obj['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['Reading']
    for fi in obj['services'][0]['data']['serviceData']['MeterReading']['datas']:
        # data.append({'Reading':fi['Reading']})
        data.append({"protocol": fi['protocol'], "id": fi['id'], "name": fi['Reading'], 'time': fi['time'], "SysTime": timeStr})

    try:
        # Reading = ''
        # bodyStr_obj = json.loads(bodyStr)
        conn = MongoClient('127.0.0.1',27017)
        db = conn.yanhua
        my_set = db.yh
        # obj = json.loads(bodyStr_obj)

        # Reading = obj['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['Reading']

        my_set.insert(data)


    except:
        pass
    # conn = MongoClient('127.0.0.1',27017)
    # db = conn.yanhua
    # my_set = db.yh
    # my_set.insert({'name':'richie'})

    return HttpResponse(Reading)

def data_his_1(request):
    bodyStr  = request.body
    write_value = "%s%s"%(bodyStr,'\n')
    with open('./logs/testlog.txt','a+') as f:
        f.write(write_value)

    return HttpResponse(write_value)