from django.shortcuts import render
import requests
from django.http import HttpResponse


def birg_com(request):
    if request.method == 'GET':
        resp2 = requests.get("https://www.tinkoff.ru/api/v1/currency_rates/")
        bir_p = resp2.json()['payload']['rates'][0]['buy']
        bir2_p = resp2.json()['payload']['rates'][1]['buy']
        resp = HttpResponse()
        resp.write(str(bir_p)+"  "+str(bir2_p))
        resp.status_code = 200
    return resp

def vk_com(request):
    if request.method == "GET":
        data_vk_vol_message = requests.get('https://api.vk.com/method/messages.getDialogs',
                             params={'v': 5.74, 'access_token': token}).json()['response']
        resp = HttpResponse()
        resp.write(str(bir_p)+"  "+str(bir2_p))
        resp.status_code = 200
    return resp



