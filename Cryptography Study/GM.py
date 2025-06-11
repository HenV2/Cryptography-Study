def GCD(a,b):
    u = 1
    g = a
    x = 0
    y = b

    while y != 0:
        q = g // y
        t = g - q * y 
        s = u - q * x
        u, g, x, y = x, y, s, t
    
    v = (g - a * u) // b
    return g, u, v

def find_inverse(a, n):
    
    g, u, v = GCD(a, n)

    return u % n 

def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b

import random

def legendre_symbol(a, p):
    a = a % p
    if a == 0:
        return 0
    exponent = (p - 1) // 2
    result = successive_squaring(a, exponent, p)
    if result == 1:
        return 1
    elif result == p - 1:
        return -1
    else:
        return 0

def encrypt_bit(m, N, a):
    if m == 0:
        c = successive_squaring(r, 2, N)
    else:
        c = (a * successive_squaring(r, 2, N)) % N
    return c


def decrypt_bit(c, p):
    ls = legendre_symbol(c, p)
    return 0 if ls == 1 else 1




p = 2309
q = 5651
N = p * q  
a = 6282665
r = random.randint(2, N - 1)
#while gcd(r, N) != 1:
#    r = random.randint(2, N - 1)

m = 0
print(f"Original message bit: {m}")


c = encrypt_bit(m, N, a)
print(f"Encrypted ciphertext: {c}")

decrypted_m = decrypt_bit(c, p)
print(f"Decrypted message bit: {decrypted_m}")


