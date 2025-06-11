def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k // 2
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
        result *= ((key ** factors[key]) - (key ** (factors[key] - 1)))
    return result

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

def computing_kth(k, b, m):
    phi_m = eulers(m)
    gcd, u, v = GCD(k, phi_m)
    if gcd == 1:
        if u < 0:
            u += phi_m
        if v < 0:
            v += k
    x = successive_squaring(b, u, m)
    return x

def rsa(code, p, q, k):
    code = str(code)
    m = str(p * q)
    result = []
    while len(code) > len(m):
        temp = ''
        for i in range(len(m) - 1):
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

def text_to_ascii_numbers(text):
    result = ''
    for char in text:
        result += str(ord(char))
    return int(result)

def ascii_numbers_to_text(number_string):
    text = ''
    for i in range(0, len(number_string), 2):
        chunk = number_string[i:i + 2]
        text += chr(int(chunk))
    return text

message = "TOBEORNOTTOBE"
ascii_code = text_to_ascii_numbers(message)
p = 12553
q = 13007
k = 79921
encrypted = rsa(ascii_code, p, q, k)
print("Encrypted:", encrypted)
modulus = p * q
decrypted = decode(k, encrypted, modulus)
plaintext = ascii_numbers_to_text(decrypted)
print("Decrypted:", plaintext)
