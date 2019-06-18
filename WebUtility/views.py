from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
# Create your views here.
from Bussiness.json_op import obtain_body_json
def data_his(request):
    body = request.body
    json_obj = json.loads(body)

    obtain_body_json(json_obj)
    # return HttpResponse(json_obj)
    # return HttpResponse(json_obj['name'])
    return None

