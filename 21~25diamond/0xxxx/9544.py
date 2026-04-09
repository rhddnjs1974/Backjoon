import sys
input = sys.stdin.readline

def characteristic(bases, mod):
    poly = [1]

    for b in bases:
        nb = (-b) % mod
        new_poly = [0] * (len(poly) + 1)

        i = 0
        while i < len(poly):
            new_poly[i] = (new_poly[i] + poly[i] * nb) % mod
            new_poly[i + 1] = (new_poly[i + 1] + poly[i]) % mod
            i += 1

        poly = new_poly

    k = len(bases)
    coeffs = [0] * (k + 1)
    t = 1
    while t <= k:
        coeffs[t] = poly[k - t]
        t += 1
    return coeffs

T = int(input())
for _ in range(T):
    k, M = map(int, input().split())
    p = list(map(int, input().split()))

    bases = [0] * k
    if k >= 1:
        bases[0] = 1 % M
    if k >= 2:
        bases[1] = 2 % M
    i = 2
    while i < k:
        bases[i] = (bases[i - 1] + bases[i - 2]) % M
        i += 1

    c = characteristic(bases, M)

    ans = 0
    t = 1
    while t <= k:
        ans = (ans + c[t] * p[k - t]) % M
        t += 1
    ans = (-ans) % M

    print(ans)
