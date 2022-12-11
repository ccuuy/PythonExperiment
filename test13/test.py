from Crypto.Util.number import *
import myRSA


def ef():
    p = getPrime(512)
    q = getPrime(512)
    flag = 123456789
    m = flag
    e = 65537
    n = p*q
    c = pow(m, e, n)

    p2 = getPrime(1024)
    q2 = getPrime(1024)
    e2 = 65537
    m2 = p+q
    n2 = p2*q2
    c2 = pow(m2, e2, n2)
    return n, e, c, n2, e2, c2, (p2+1)*(q2+1)


def decryption(n, e, c, n2, e2, c2, hole):
    phi_n2 = 2*n2 - hole + 2
    d2 = myRSA.InvMod(e2, phi_n2)
    m2 = myRSA.RSADecryption(c2, n2, d2)
    phi_n1 = n - m2 + 1
    d = myRSA.InvMod(e, phi_n1)
    m = myRSA.RSADecryption(c, n, d)
    return m


n, e, c, n2, e2, c2, hole = ef()

flag = decryption(n, e, c, n2, e2, c2, hole)
print("flag=", flag)
