# 6.Eratoschenes筛法求素数

a = list(range(2, 1001))

def Eratoschenes(x):
    return x % y != 0 or x == y

for i in a:
    y = i
    a = list(filter(Eratoschenes, a))
print(a)

