def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b

def prime_factors(n):
    result = {}
    x = 2 
    while x <= n:
        while n % x == 0:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
            n //= x 
        x += 1 

    return result 

def eulers(n):
    factors = prime_factors(n)
    result = 1
    for key in factors:
        result *= ((key**factors[key])-(key**(factors[key]-1)))
    
    return result 

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


#print(prime_factors(1073))
#print(eulers(1073))
    
def computing_kth(k, b, m):
    
    phi_m = eulers(m)

    gcd, u, v = GCD(k,phi_m)

    if gcd == 1:
        if u < 0:
            u += phi_m 
        if v < 0:
            v += k

    x = successive_squaring(b, u, m)  

    return x

#print(computing_kth(131, 758, 1073))

def rsa(code, p, q, k):

    print(f'Orginial Code: {code}')
    code = str(code)
    m = str(p*q)

    result = []

    while len(code) > len(m):
        temp = ''
        for i in range(len(m)-1):
            temp += code[0]
            code = code[1:]
        result.append(temp)
    result.append(code)

    new_result = []

    for array in result:
        new_result.append(successive_squaring(int(array), k, int(m)))

    return new_result

def decode(k, code, m):
    result = ''
    
    for b in code:
        array = computing_kth(k, b, m)

        result += str(array)

    return result

#print(rsa(30251215252824253030251215, 12553, 13007, 79921))

#print(decode(79921, rsa(30251215252824253030251215, 12553, 13007, 79921), 163276871))

def RSAsig(p, q, e, D):

    n = p*q
    phim = (p-1)*(q-1)


    d = find_inverse(e, phim)

    return successive_squaring(D, d, n)

p = 1223
q = 1987
e = 948047
D = 1070777

print(RSAsig(p, q, e, D))

def RSAverify(p, q, e, D, S):
    n = p*q
    return successive_squaring(S, e, n) == D

print(RSAverify(p, q, e, D, RSAsig(p, q, e, D)))

    
