import GenRSAKeys


def encryption(info, N, e):
    return pow(info, e, N)


def decryption(CipherText, N, d):
    return pow(CipherText, d, N)


pub, pri = GenRSAKeys.GenRSAKeys()
info = 452422
CipherText = encryption(info, pub[1], pub[0])
print('密文', CipherText)
print('解密', decryption(CipherText, pri[1], pri[0]))
