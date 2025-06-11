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

def diffie_hellman(p, g, a, b):
    
    A = successive_squaring(g, a, p) #A = g^a mod p
    B = successive_squaring(g, b, p) #B = g^b mod p
    
    key1 = successive_squaring(B, a, p) 
    key2 = successive_squaring(A, b, p)

    print(key1, key2)   

    return A, B, key1

def elgamal_encrypt(p, g, A, m, k):

    c1 = successive_squaring(g, k, p)
    c2 = (m * successive_squaring(A, k, p)) % p
    return c1, c2

def elgamal_decrypt(p, a, c1, c2):
    s = successive_squaring(c1, a, p)
    s_inv = find_inverse(s, p) 
    m = (c2 * s_inv) % p
    return m

#print('Encryption:')
#print(elgamal_encrypt(467, 2, successive_squaring(2, 153, 467), 331, 197))
#print('Decryption:')
#print(elgamal_decrypt(467, 153, 87, 57))

def elgamal_sign(p, g, a, D, k):

    A = successive_squaring(g, a, p)
    S1 = successive_squaring(g, k, p)
    k_inv = find_inverse(k, p - 1)
    S2 = ((D - a * S1)*k_inv) % (p - 1)

    return S1, S2, A

def elgamal_verify(p, g, A, D, S1, S2):

    compute = (successive_squaring(g, D, p))

    a = successive_squaring(A, S1, p)
    b = successive_squaring(S1, S2, p)
    check = (a * b) % p
 
    if check == compute:
        print("Signature is valid")
    else:
        print("Signature is invalid")

p = 21739
g = 7
a = 15140
D = 5331
k = 10727

S1, S2, A = elgamal_sign(p, g, a, D, k)
print(S1, S2)

elgamal_verify(p, g, A, D, S1, S2)