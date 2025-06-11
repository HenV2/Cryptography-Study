def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b

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

def elgamal_encrypt(p, g, A, m, k):

    c1 = successive_squaring(g, k, p)
    c2 = (m * successive_squaring(A, k, p)) % p
    return c1, c2

def elgamal_decrypt(p, a, c1, c2):
    s = successive_squaring(c1, a, p)
    s_inv = find_inverse(s, p) 
    m = (c2 * s_inv) % p
    return m

print('Encryption:')
print(elgamal_encrypt(467, 2, successive_squaring(2, 153, 467), 331, 197))
print('Decryption:')
print(elgamal_decrypt(467, 153, 87, 57))