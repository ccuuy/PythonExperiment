def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
# 扩展欧几里得算法


def ExtGcd(a, m):  # a<m
    if a == 0:
        return 0, 1, m  # m = 1 * m + 0 * a, m是最大公因子
    else:
        x, y, MaxCmnFct = ExtGcd(m % a, a)  # 获得本层递归的结果
        x, y = y-(m//a)*x, x  # 计算上层递归结果
    return x, y, MaxCmnFct


# 扩展欧几里得算法非递归实现
def ExtGcd_NonRecursive(a, m):
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # //是整数除法运算符
        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
    return u1, u2, u3


# 求模逆
def InvMod(a, m):
    if gcd(a, m) != 1:
        return None  # 如果a和m不互质，则不存在模逆
    return ExtGcd_NonRecursive(a, m)[0]


def RSAEncryption(info, N, e):
    return pow(info, e, N)


def RSADecryption(CipherText, N, d):
    return pow(CipherText, d, N)
