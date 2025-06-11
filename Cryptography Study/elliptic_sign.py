import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def GCD(a, b):
    u, g, x, y = 1, a, 0, b
    while y != 0:
        q = g // y
        g, y = y, g - q * y
        u, x = x, u - q * x
    v = (g - a * u) // b if b != 0 else 0
    return g, u, v


def find_inverse(a, n):
    
    g, u, v = GCD(a, n)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {n}")
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
    
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    
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

def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b


def miller_rabin(a, n):
    k = 0
    m = n - 1
    while m % 2 == 0:
        k += 1
        m = m // 2
    b = successive_squaring(a, m, n)
    if b == 1:
        return 'Test Fails'
    for i in range(k):
        if b == n - 1:
            return 'Test Fails'
        b = successive_squaring(b, 2, n)
    return 'Composite'



def get_order(P, A, p):
    Q = P
    n = 1
    while Q != 'O':
        Q = elliptic_curve_add(Q, P, A, p)
        n += 1
    return n



def find_point(A, B, p):
    points = []

    for x in range(p):
        for y in range(p):
            if (y**2 - x**3 - A*x - B) % p == 0:
                points.append((x, y))

    return points


def ecdsa_keygen(G, A, p, q):
    s = random.randint(1, q - 1)
    V = doubleandadd(G, s, A, p)
    return s, V


def ecdsa_sign(d, s, G, A, p, q):
    while True:
        e = random.randint(1, q - 1)
        eG = doubleandadd(G, e, A, p)
        s1 = eG[0] % q
        if s1 == 0:
            continue
        e_inv = find_inverse(e, q)
        s2 = ((d + s1 * s) * e_inv) % q
        if s2 != 0:
            break
    return s1, s2

def ecdsa_verify(d, s1, s2, V, G, A, p, q):
    s2_inv = find_inverse(s2, q)
    v1 = (d * s2_inv) % q
    v2 = (s1 * s2_inv) % q
    P1 = doubleandadd(G, v1, A, p)
    P2 = doubleandadd(V, v2, A, p)
    R = elliptic_curve_add(P1, P2, A, p)
    return R != 'O' and R[0] % q == s1


A, B, p = 2, 3, 997
points = find_point(A, B, p)
G = None
q = None
for pt in points:
    ord_pt = get_order(pt, A, p)
    print(pt, ord_pt)
    if ord_pt > 100 and is_prime(ord_pt):
        G = pt
        q = ord_pt
    


print(f"G: {G}, order: {q}")
s, V = ecdsa_keygen(G, A, p, q)
print("S, V:", s, V)


d = 7
s1, s2 = ecdsa_sign(d, s, G, A, p, q)
print("Signature:", (s1, s2))

verify = ecdsa_verify(d, s1, s2, V, G, A, p, q)
print("Verify", verify)
