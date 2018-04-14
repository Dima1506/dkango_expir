from django.shortcuts import render
import requests
import re
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
        cookies = {
            'remixsid': '0b876b70114513ab69c6b78bc9288322b4591fff806515e75e184'
        }
        data = requests.get('https://vk.com/im', cookies=cookies)
        arr = re.search(r'</div><div class="Bell__counter">(\d+)</div></a>', data.text)
        data_vk_vol_message = requests.get('https://api.vk.com/method/messages.getDialogs',
                             params={'v': 5.74, 'access_token': token}).json()['response']
        data_vk_vol_friends = requests.get('https://api.vk.com/method/friends.getRequests',
                    params={'v': 5.74, 'access_token': token}).json()['response']
        count_unread = 0
        for i in data_vk_vol_message['items']:
            if 'unread' in i:
                count_unread = count_unread + 1
        resp = HttpResponse()
        resp.write(str(data_vk_vol_friends['count'])+"_"+str(count_unread)+"_"+arr.group(1))
        resp.status_code = 200
    return resp


# NewsAPI.org

def news_com(request, num):
    if request.method == 'GET':
        resp2 = requests.get("https://newsapi.org/v2/top-headlines?country=ru&apiKey=38b28e3e9928480ba1180cf244e0b8fd")
        resp = HttpResponse()
        resp.write(resp2.json()['articles'][int(num)]['title'])
        resp.status_code = 200
    return resp



