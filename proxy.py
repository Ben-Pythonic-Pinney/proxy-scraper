# HTTP/s proxy-scaper
# Created By: Ben Pinney
# Example: python[version] proxy.py

from bs4 import BeautifulSoup
import requests

r = requests.get('https://free-proxy-list.net')

command = BeautifulSoup(r.content, 'html.parser')

result = command.find('tbody')

for i in result:
    print(f'{i.find_all("td")[0].text}:{i.find_all("td")[1].text}')
