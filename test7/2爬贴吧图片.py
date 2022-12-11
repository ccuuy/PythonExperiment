import urllib.request
import re
link = "https://tieba.baidu.com/p/2460150866?pn="
pattern1 = re.compile('<img.*?class="BDE_Image".*?>')
pattern2 = re.compile('(?<=src=").*?(?=")')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
for i in range(1, 61):
    print("爬取第", i, "页中的图片...")
    req = urllib.request.Request(url=link+str(i), headers=headers)
    fp = urllib.request.urlopen(req)
    contents = fp.read().decode()
    pics = pattern1.findall(str(contents))
    pics_src = list()
    for j in pics:
        pics_src.append(pattern2.findall(j)[0])

    for j in pics_src:
        if 'https' in j:
            fpic = urllib.request.urlopen(j)
            f = open("./pics/"+j[-15:], 'wb')
            f.write(fpic.read())
            f.close()
