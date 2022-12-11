import requests
from bs4 import BeautifulSoup
import re
import time
url = 'http://www.aidusk.com/t/19597/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


reqst = requests.get(url, headers=headers)
reqst.encoding = 'utf-8'

li = BeautifulSoup(str(BeautifulSoup(reqst.text, 'lxml').find_all(
    'div', attrs={'class': 'book_con_list'})[1]), 'lxml').find_all('li')

for i in li:
    i_bs = BeautifulSoup(str(i), 'lxml')
    name = i_bs.a.string
    link = i_bs.a['href']

    newReqst = requests.get(url+link, headers=headers)
    newReqst.encoding = 'utf-8'
    chapterContent = BeautifulSoup(newReqst.text, 'lxml').find(
        'div', attrs={'id': 'content'})
    print("正在获取"+name)
    f = open('./余罪/'+name+'.txt', 'w', encoding='utf-8')
    chapterContent = str(chapterContent)
    chapterContent = re.sub('<.*?>', '', chapterContent)
    f.write(chapterContent)
    f.close()
    time.sleep(5)  # 防止触发反爬
