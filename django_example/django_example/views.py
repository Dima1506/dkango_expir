from django.shortcuts import render
import requests
import re
from django.http import HttpResponse
import lxml.html

def birg_com(request):
    if request.method == 'GET':
        resp2 = requests.get("https://www.tinkoff.ru/api/v1/currency_rates/")
        bir_p = resp2.json()['payload']['rates'][0]['buy']
        bir2_p = resp2.json()['payload']['rates'][1]['buy']
	resp3 = requests.get("https://api.blockchain.info/stats").json()["market_price_usd"]
        resp = HttpResponse()
        resp.write(str(bir_p)+"_"+str(bir2_p)+ '_' + str(int(round(resp3, 0))))
        resp.status_code = 200
    return resp

def vk_com(request):
    if request.method == "GET":
        token = '08e35f615f6579bda204ef012617ea8703349210c983a34068f0e87af95a371be9559cbe0ef0ad969358d'

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Connection':'keep-alive',
		'DNT':'1'
	}

	url = 'https://vk.com/'
	session = requests.session()
	data = session.get(url, headers=headers)
	page = lxml.html.fromstring(data.content)
	form = page.forms[0]
	form.fields['email'] = '+79969236197'
	form.fields['pass'] = 'cxzaq15061999'
	response = session.post(form.action, data=form.form_values())
	data = session.get('https://vk.com/im')

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



