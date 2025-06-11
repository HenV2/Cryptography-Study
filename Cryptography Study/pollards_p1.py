from GCD import GCD
from GCD import successive_squaring

def pollards_factorization(n, B):

    a = 2
    j = 2

    while j <= B:
        a = successive_squaring(a, j, n)
        d = GCD(a - 1, n)[0]
        if 1 < d < n:
            return d
        j += 1
    
    return None

print(pollards_factorization(13927189, 20))
print(pollards_factorization(6994241, 20))


