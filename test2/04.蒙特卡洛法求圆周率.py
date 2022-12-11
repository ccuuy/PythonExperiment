import random


for i in [100, 1000, 10000, 100000, 1000000, 10000000]:
    times = 0
    for j in range(i):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        coo = pow(x, 2) + pow(y, 2)
        if coo < 1:
            times += 1
    print("模拟" + str(i) + "次时,圆周率为" + str(4 * times/i))
