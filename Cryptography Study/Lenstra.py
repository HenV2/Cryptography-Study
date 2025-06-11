import random

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

def lenstra(N, P, A):

    j = 2
    point = P

    while True:
        print(j, point)
        try:
            d = GCD(point[0], N)[0]  
            if d == 1:
                point = doubleandadd(point, j, A, N)
                j += 1
            else:
                if 1 < d < N:
                    return d  
                elif d == N:
                    return None
        except:
            if 1 < d < N:
                return d  
            elif d == N:
                return None


def getpoint(A, B, p):

    while True:
        x = random.randint(0, p-1)
        y = random.randint(0, p-1)

        if (y**2 - x**3 - A*x - B) % p == 0:
            points = (x, y)
            return points
      

print('BOOK EXAMPLE')
print('--------------------------------------')
print(lenstra(6887, (1512, 3166), 14))

print('RANDOM POINT')

P = getpoint(14, 19, 6887)
print(P)
print(lenstra(6887, P, 14))






    