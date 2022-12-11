import random


# Rabin-Miller素性检测
def RabinMiller(num):

    # num -1 = 2^{t}*s
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    # 进行五次检测
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v, 2, num)
    return True
