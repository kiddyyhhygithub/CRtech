from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from Bussiness.json_op import obtain_body_json
import Classes.Reading as rd
import time
from DBHelper.DBUtility import DBUtility
from Classes.Meter import Meter
def index(request):
    return HttpResponse("ok")

def data_his(request):
    body = request.body
    # json_obj = json.loads(body)
    # obtain_body_json(json_obj)
    try:
        json_obj = json.loads(body)

        obtain_body_json(json_obj)
    except:
        pass
    # return HttpResponse(json_obj)
    # return HttpResponse(json_obj['name'])
    # with open('log.txt',"a+") as f:
    #     f.write(body)
    return HttpResponse(body)

def disp_his(request):


    data = [ ]
    # for i in range(2):
    #     reading = rd.Reading()
    #     reading.name = i
    #     data.append(reading)
    db = DBUtility()
    for d in db.get_data():
        meter = Meter()
        meter.SysTime = d['SysTime']
        meter.Time = d['time']
        meter.MeterID = d['id']
        meter.Protocol = d['protocol']
        meter.Reading = d['Reading']
        data.append(meter)
    title = '水表信息'

    content = {"title":title,
               'b':'b',
               "data":data,
               }
    return  render(request,'index/showdata.html',content)

def insert_data_his(request):
    '''
    通过传入数据 插入数据至数据库
    :param request:
    :return:
    '''
    result = False
    data = []
    req = request.body
    
    try:
        body = json.loads(req)
    except:
        print()
    try:
        body = json.loads( req.decode('utf-8') )
    except:
        pass
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for fi in body['services'][0]['data']['serviceData']['MeterReading']['datas']:
        data.append({"protocol":fi['protocol'],"id":fi['id'],"Reading": fi['Reading'],'time':fi['time'],"SysTime":timeStr})
        pass

    try:
        db = DBUtility()
        db.insert_data(data)
        result = True
    except:
        pass
    return HttpResponse(result)