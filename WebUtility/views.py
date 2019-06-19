from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from Bussiness.json_op import obtain_body_json
import Classes.Reading as rd
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
    reading1 = rd.Reading()
    reading1.name = 'yanhua'
    data.append(reading1)
    reading2 = rd.Reading()
    reading2.name = 'huyu'
    data.append(reading2)

    title = '水表信息'

    content = {"title":title,
               'b':'b',
               "data":data,
               }
    return  render(request,'index/showdata.html',content)
