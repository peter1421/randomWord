import requests
from bs4 import BeautifulSoup

url = 'https://hbl917070.cf/baha_analysis/article?po_type=1&userid=fil12385ki'

response = requests.get(url)

root = BeautifulSoup(response.text, "html.parser")
title = root.find_all('a', target="_blank")

for x in title:
    print(x)
