# -* coding:utf-8 -*-
import requests
url = 'https://api.douban.com/v2/book/search'
params = {
    'q':'python',
    'start':0,
    'count':20}
response = requests.get(url, params=params)
f = open("d://douban-" + params['q'] + ".json", 'wb')
f.write(response.content)
f.close()
