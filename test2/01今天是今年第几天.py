import time
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
today = time.localtime()
if today.tm_year % 4 == 0:
    month[1] = 29
res = sum(month[:today.tm_mon-1]) + today.tm_mday
print("今天是" + str(today.tm_year) + "年第" + str(res) + "天")
