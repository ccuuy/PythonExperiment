# 7.随机生成密码

import random
import string


def isStrong(ikey):
    r = [0] * 4

    for ch in ikey:
        if not r[0] and ch in string.digits:
            r[0] = 1
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = 1
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = 1
        elif not r[3] and ch in string.punctuation:
            r[3] = 1
        if (sum(r) == 4):
            return print("强密码")
    return print("弱密码")


key = "".join(random.sample(
    string.punctuation + string.ascii_letters + string.digits, random.randint(8, 25)))
print(key)
isStrong(key)
