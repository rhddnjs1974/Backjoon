import sys

input = sys.stdin.readline
MOD = 1000000007

def c_add(a, b):
    return (((a[0] + b[0]) % MOD), ((a[1] + b[1]) % MOD))

def c_sub(a, b):
    return (((a[0] - b[0]) % MOD), ((a[1] - b[1]) % MOD))

def c_mul(a, b):
    return ((((a[0] * b[0]) - (a[1] * b[1])) % MOD), (((a[0] * b[1]) + (a[1] * b[0])) % MOD))

def c_smul(a, k):
    return (((a[0] * k) % MOD), ((a[1] * k) % MOD))

def c_inv(a):
    d = (((a[0] * a[0]) + (a[1] * a[1])) % MOD)
    invd = pow(d, (MOD - 2), MOD)
    return (((a[0] * invd) % MOD), (((-a[1]) * invd) % MOD))

def c_pow(a, e):
    r = (1, 0)
    b = a
    while e > 0:
        if (e & 1) == 1:
            r = c_mul(r, b)
        b = c_mul(b, b)
        e >>= 1
    return r

N, L, M, R = map(int, input().split())
T = (L + M + R)
invT = pow(T, (MOD - 2), MOD)

pM = ((M % MOD) * invT) % MOD
pL = ((L % MOD) * invT) % MOD
pR = ((R % MOD) * invT) % MOD

z = (pM, ((pR - pL) % MOD))

if (z[0] % MOD) == 1 and (z[1] % MOD) == 0:
    print(((N % MOD) * (N % MOD)) % MOD)
else:
    n = (N - 1)
    if n == 0:
        print(0)
    else:
        zn = c_pow(z, n)
        zn1 = c_mul(zn, z)

        one = (1, 0)
        den = c_sub(one, z)
        invden = c_inv(den)
        invden2 = c_mul(invden, invden)

        G1 = c_mul(c_mul(z, c_sub(one, zn)), invden)

        t2 = c_sub(one, c_smul(zn, N))
        t2 = c_add(t2, c_smul(zn1, n))
        G2 = c_mul(c_mul(z, t2), invden2)

        S1 = G1[0] % MOD
        S2 = G2[0] % MOD

        ans = (N + (2 * (( (N * S1) % MOD ) - S2)) ) % MOD
        print(ans % MOD)