prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
# n < 3,317,011,064,679,887,385,961,981
def power(a,b,c):
    if b==1:
        return a
    if b==0:
        return 1
    if b%2==0:
        return power(a,b//2,c)**2 % c
    else:
        return a*(power(a,b//2,c) ** 2) % c


def miller_rabin(n, a):
    r = 0
    d = n-1
    while (d%2==0):
        r += 1
        d //= 2

    x = power(a, d, n)
    if x == 1 or x + 1 == n:
        return 1

    for i in range(0, r - 1):
        x = power(x, 2, n)
        if x + 1 == n:
            return 1

    return 0

def isprime(n):
    if n in prime:
        return 1
    if n == 1 or n % 2 == 0:
        return 0
    for p in prime:
        if not miller_rabin(n, p):
            return 0
    return 1

print(isprime(99007))