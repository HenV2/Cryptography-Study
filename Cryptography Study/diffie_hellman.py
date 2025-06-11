def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b

def diffie_hellman(p, g, a, b):
    
    A = successive_squaring(g, a, p) #A = g^a mod p, Alice's public key
    B = successive_squaring(g, b, p) #B = g^b mod p, Bob's public key
    
    key1 = successive_squaring(B, a, p) 
    key2 = successive_squaring(A, b, p)

    if key1 == key2:
        return A, B, key1
    else:
        print("Keys do not match")

A, B, key1 = diffie_hellman(941, 627, 347, 781)
print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Shared secret key: {key1}")

