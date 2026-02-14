import math

b,d,a = map(int,input().split())

k_max = a // b
max_t = len(str(a))

def ok(t):
    m = 10 ** t

    if d == 0:
        x = 0
    else:
        x = d * ((m - 1) // 9)

    g = math.gcd(b, m)
    if x % g != 0:
        return False

    b1 = b // g
    x1 = x // g
    m1 = m // g

    inv = pow(b1, -1, m1)
    k0 = (x1 * inv) % m1
    if k0 == 0:
        k0 = m1

    return k0 <= k_max

lo = 0
hi = max_t
while lo < hi:
    mid = (lo + hi + 1) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid-1

print(lo)
