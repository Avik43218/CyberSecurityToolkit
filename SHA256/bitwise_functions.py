def rotr(x, n):
    return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def Σ0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def Σ1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def σ0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def σ1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)
