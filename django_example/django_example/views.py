from django.shortcuts import render
import requests
from django.http import HttpResponse


def birg_com(request):
    if request.method == 'GET':
        resp2 = requests.get("https://www.tinkoff.ru/api/v1/currency_rates/")
        bir_p = resp2.json()['payload']['rates'][0]['buy']
        bir2_p = resp2.json()['payload']['rates'][1]['buy']
        resp = HttpResponse()
        resp.write(str(bir_p)+"_"+str(bir2_p))
        resp.status_code = 200
    return resp

def vk_com(request):
    if request.method == "GET":
        token = '08e35f615f6579bda204ef012617ea8703349210c983a34068f0e87af95a371be9559cbe0ef0ad969358d'
        data_vk_vol_message = requests.get('https://api.vk.com/method/messages.getDialogs',
                             params={'v': 5.74, 'access_token': token}).json()['response']
        data_vk_vol_friends = requests.get('https://api.vk.com/method/friends.getRequests',
                    params={'v': 5.74, 'access_token': token}).json()['response']
        count_unread = 0
        for i in data_vk_vol_message['items']:
            if 'unread' in i:
                count_unread = count_unread + 1
        resp = HttpResponse()
        resp.write(str(data_vk_vol_friends['count'])+"  "+str(count_unread))
        resp.status_code = 200
    return resp



