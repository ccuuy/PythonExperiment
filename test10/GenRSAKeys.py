import GenBigPrimeNum
import InvMod


def GenRSAKeys():
    p = GenBigPrimeNum.RandPrime(1024)
    q = GenBigPrimeNum.RandPrime(1024)
    N = p * q
    phi_N = (p-1) * (q-1)
    e = 65537
    d = InvMod.InvMod(e, phi_N)
    return [[e, N], [d, N]]
