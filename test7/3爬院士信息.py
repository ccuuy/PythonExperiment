import urllib.request
import re
import os

link = "https://www.cae.cn"
link1 = link + "/cae/html/main/col48/column_48_1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


pattern1 = re.compile('<li class="name_list">.*?</li>')
pattern2 = re.compile(
    '(?<=<li class="name_list"><a href=").*?(?=")')  # 匹配院士个人链接
pattern3 = re.compile('(?<=target="_blank">).*?(?=</a></li>)')  # 匹配院士姓名

pattern4 = re.compile('<div class="info_img">.*?</div>')
pattern5 = re.compile('(?<=src=").*?(?=")')  # 匹配院士照片链接1

pattern6 = re.compile('<div class="intro">.*?</div>')
pattern7 = re.compile('(?<=&ensp;&ensp;&ensp;&ensp;).*?(?=</p>)')  # 匹配院士介绍


# 中文解码
def cnDecode(codes):
    j = 0
    for i in codes:
        i = eval(repr(i).replace('\\\\', '\\'))
        i = i.encode('raw_unicode_escape').decode()
        codes[j] = i
        j += 1


links = list()  # 院士个人链接
names = list()  # 院士姓名


req = urllib.request.Request(url=link1, headers=headers)
fp = urllib.request.urlopen(req)
contents = fp.read()
info = pattern1.findall(str(contents))
for i in info:
    links.append(pattern2.findall(i)[0])
    names.append(pattern3.findall(i)[0])

cnDecode(names)
pwd = os.getcwd()


k = 0
for i in links:
    req = urllib.request.Request(url=link+i, headers=headers)
    fp1 = urllib.request.urlopen(req)
    contents1 = fp1.read()
    picinfo = pattern4.findall(str(contents1))
    introinfo = pattern6.findall(str(contents1))

    piclink = link + pattern5.findall(picinfo[0])[0]
    maininfo = pattern7.findall(introinfo[0])

    # 创建院士个人文件夹
    os.mkdir(pwd+"/info/"+names[k])

    # 写院士信息
    fh = open("./info/"+names[k]+"/"+names[k]+".txt", "w")
    cnDecode(maininfo)
    for j in maininfo:
        fh.write(j+'\n')
    fh.close()

    # 写院士照片
    fh = open("./info/"+names[k]+"/"+names[k]+".jpg", "wb")
    for j in piclink:
        req = urllib.request.Request(url=piclink, headers=headers)
        fp2 = urllib.request.urlopen(req)
        contents2 = fp2.read()
        fh.write(contents2)
    fh.close()
    k += 1
