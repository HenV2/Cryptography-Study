def GCD(a, b):
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

def elliptic_curve_add(P1, P2, A, p):
    if P1 == 'O':
        return P2
    if P2 == 'O':
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and (y1 + y2) % p == 0:
        return 'O'

    if x1 == x2 and y1 == y2:
        slope = (3 * x1**2 + A) * find_inverse(2 * y1, p)
    else:
        slope = (y2 - y1) * find_inverse(x2 - x1, p)

    x3 = slope**2 - x1 - x2
    y3 = slope * (x1 - x3) - y1

    return (x3 % p, y3 % p)


def doubleandadd(P, n, A, p):

    Q = P
    
    R = 'O'

    while n > 0:
        if n % 2 == 1:
            R = elliptic_curve_add(R, Q, A, p)
        Q = elliptic_curve_add(Q, Q, A, p)
        n //= 2

    return R


def elliptic_diffie_hellman(P, n1, n2, A, p):

    Qa = doubleandadd(P, n1, A, p)
    Qb = doubleandadd(P, n2, A, p)

    shared_key1 = doubleandadd(Qb, n1, A, p)
    shared_key2 = doubleandadd(Qa, n2, A, p)

    if shared_key1 != shared_key2:
        raise ValueError("Shared keys do not match")

    return shared_key1

#print(elliptic_diffie_hellman((920, 303), 1194, 1759, 324, 3851))

def elliptic_key_encrypt(M, k, P, Q, A, p):
    
    c1 = doubleandadd(P, k, A, p)
    kq = doubleandadd(Q, k, A, p)
    
    c2 = elliptic_curve_add(M, kq, A, p)

    return c1, c2


def elliptic_key_decrypt(C1, C2, n, A, p):
    
    nC1 = doubleandadd(C1, n, A, p)
    
    if nC1 == 'O':
        minus_nC1 = 'O'
    else:
        x, y = nC1
        minus_nC1 = (x, (-y) % p)
    
    M = elliptic_curve_add(C2, minus_nC1, A, p)
    
    return M

A = 3
p = 13
P = (2, 10)
n = 4
Q = doubleandadd(P, n, A, p)
M = (1, 8)
k = 5

print('Encryption:')
c1, c2 = elliptic_key_encrypt(M, k, P, Q, A, p)
print(c1, c2)
print('Decryption:')
print(elliptic_key_decrypt(c1, c2, n, A, p))

'''
A = 324
p = 3851
P = (920, 303)
n = 1194
Q = doubleandadd(P, n, A, p)
M = (3681, 612)
'''
import random

def random_find_points(A, B, p):
    points = []

    while len(points) <= 27:
        x = random.randint(0, p-1)
        y = random.randint(0, p-1)

        if (y**2 - x**3 - A*x - B) % p == 0:
            points.append((x, y))

    return points

points = random_find_points(5, 24, 947)

'''

def random_find_points(A, B, p):
    points = []

    while len(points) <= 27:
        x = random.randint(0, p-1)
        y = random.randint(0, p-1)

        if (y**2 - x**3 - A*x - B) % p == 0:
            points.append((x, y))

    return points

points = random_find_points(5, 24, 947)

'''
def get_order(P, A, p):
    Q = P
    n = 1

    while Q != 'O':
        Q = elliptic_curve_add(Q, P, A, p)
        n += 1

    return n


def ecdsa_keygen(G, A, p, q):

    s = random.randint(1, q - 1)      
    V = doubleandadd(G, s, A, p)     
    return s, V  

def ecdsa_sign(d, s, G, A, p, q):
        e = random.randint(1, q - 1) 
        eG = doubleandadd(G, e, A, p)

        s1 = eG[0] % q

        e_inv = find_inverse(e, q)
        s2 = ((d + s1 * s) * e_inv) % q

        return s1, s2

def ecdsa_verify(d, s1, s2, V, G, A, p, q):

    s2_inv = find_inverse(s2, q)

    v1 = (d * s2_inv) % q
    v2 = (s1 * s2_inv) % q

    P1 = doubleandadd(G, v1, A, p)
    P2 = doubleandadd(V, v2, A, p)

    verify = elliptic_curve_add(P1, P2, A, p)

    if verify[0] % q == s1:
        return True
    else:
        return False
    

    
for point in points:
    print(point)
    print(get_order(point, 5, 947))