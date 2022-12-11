import requests
from bs4 import BeautifulSoup
import re
import time
url = 'https://www.ncdc.noaa.gov/sotc/global/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

a = []
for i in range(2019, 2023):
    for j in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        a.append(str(i)+str(j))

for i in a:
    reqst = requests.get(url+i, headers=headers)
    reqst.encoding = 'utf-8'

    ul = BeautifulSoup(str(BeautifulSoup(reqst.text, 'lxml').find(
        'div', attrs={'id': 'sotc-content'})), 'lxml').find('div', attrs={'class': 'clear'}).next_sibling.next_sibling
    ul = str(ul)
    ul1 = re.sub('<.*?>', '', ul)
    print(i)
    print(ul1)
