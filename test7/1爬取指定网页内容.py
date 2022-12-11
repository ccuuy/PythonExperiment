import urllib.request
url = input()
link = "https://"+url
fp = urllib.request.urlopen(link)

contents = fp.read().decode('utf-8')

f = open(str(url[0:3])+".html", 'w', encoding='utf-8')
f.write(str(contents))
f.close
