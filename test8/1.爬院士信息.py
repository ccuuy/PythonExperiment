import requests
from bs4 import BeautifulSoup

link = "https://www.cae.cn"
link1 = link + "/cae/html/main/col48/column_48_1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


reqst = requests.get(link1, headers=headers)
contents = BeautifulSoup(reqst.text, 'lxml')
li = contents.find_all('li', attrs={'class': 'name_list'})

for i in li:
    i_bs = BeautifulSoup(str(i), 'lxml')
    name = i_bs.a.string
    introLink = i_bs.a['href']
    newLink = link+introLink
    newReqst = requests.get(newLink, headers=headers)
    newContents = BeautifulSoup(newReqst.text, 'lxml')
    introInfo = newContents.find('div', attrs={'class': 'intro'}).find_all('p')
    introInfo1 = str(introInfo[0].string +
                     introInfo[1].string+introInfo[2].string)
    print('已获取'+name+'院士信息')
    f = open('./info/'+name+'.txt', 'w', encoding='utf-8')
    f.write(introInfo1)
    f.close()
