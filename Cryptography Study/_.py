def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = (a * a) % m
        k = k//2

    return b

def successive_squaring2(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = a * b
        a = a * a
        k = k//2

    return b

print(successive_squaring(2, 1000, 2379))
print(pow(2, 1000, 2379))
print(successive_squaring(567, 1234, 4321))
print(pow(567, 1234, 4321))
