# -*- coding: utf-8 -*-
import requests

id = "3112503"
url = "https://api.douban.com/v2/book/" + id
response = requests.get(url)
f = open("d://douban-" + id + ".json", 'wb')
f.write(response.content)
f.close()
