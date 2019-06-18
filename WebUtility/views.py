from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
# Create your views here.
from Bussiness.json_op import obtain_body_json
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

