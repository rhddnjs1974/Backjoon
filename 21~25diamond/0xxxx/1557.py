import sys
input = sys.stdin.readline

def count_sqf(x):
    r = int(x**0.5)
    s = 0
    for i in range(1, r + 1):
        s += mu[i] * (x // (i * i))
    return s

K = int(input())
MA = 2 * K
ll = int(MA**0.5) + 1

mu = [1] * (ll + 1)
is_prime = [True] * (ll + 1)
mu[0] = 0
primes = []

for i in range(2, ll + 1):
    if is_prime[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        t = i * p
        if t > ll:
            break
        is_prime[t] = False
        if i % p == 0:
            mu[t] = 0
            break
        else:
            mu[t] = -mu[i]
            
l, h = 1, MA
while l < h:
    mid = (l + h) // 2
    if count_sqf(mid) >= K:
        h = mid
    else:
        l = mid + 1

print(l)
