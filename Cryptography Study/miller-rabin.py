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

def miller_rabin(a, n):

    #if GCD(a, n)[0] < n:
    #    return 'Composite'
    
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

print(miller_rabin(2, 561))
print(miller_rabin(17, 172947529))
print(miller_rabin(3, 172947529))
print(miller_rabin(23, 172947529))