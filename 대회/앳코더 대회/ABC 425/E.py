import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

import sys
import math

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)

def inv_mod(a, m):
    a %= m
    g, x, _ = egcd(a, m)
    return x % m

def factorize(n):
    res = []
    x = n
    for p in range(2, math.isqrt(x) + 1):
        if x % p == 0:
            e = 0
            pe = 1
            while x % p == 0:
                x //= p
                e += 1
                pe *= p
            res.append((p, e, pe))
    if x > 1:
        res.append((x, 1, x))
    return res

def build_tables_for_prime_power(p, pe):
    exp = [0] * (5001)
    pref = [1] * (5001)
    for i in range(1, 5001):
        t = i
        cnt = 0
        while t % p == 0:
            t //= p
            cnt += 1
        exp[i] = exp[i - 1] + cnt
        pref[i] = (pref[i - 1] * (t % pe)) % pe
    return exp, pref

def crt_pair(x1, m1, x2, m2):
    rhs = (x2 - x1) % m2
    t = (rhs * inv_mod(m1 % m2, m2)) % m2
    x = (x1 + t * m1) % (m1 * m2)
    return x, m1 * m2

def crt_all(residues, moduli):
    x = 0
    m = 1
    for r, mod in zip(residues, moduli):
        x, m = crt_pair(x, m, r % mod, mod)
    return x % m

T,M = map(int,input().split())

factors = factorize(M)
mod_list = [pe for (_, _, pe) in factors]

tables = []
for (p, e, pe) in factors:
    tables.append((p, e, pe, *build_tables_for_prime_power(p, pe)))

out_lines = []
for _ in range(T):
    N = int(input())
    Cs = list(map(int,input().split()))
    S = sum(Cs)

    residues = []
    for (p, e, pe, exp, pref) in tables:

        V = exp[S]
        for c in Cs:
            V -= exp[c]

        if V >= e:
            residues.append(0)
            continue

        den = 1
        for c in Cs:
            den = (den * pref[c]) % pe
        unit = (pref[S] * inv_mod(den, pe)) % pe

        res_pe = (unit * pow(p, V, pe)) % pe
        residues.append(res_pe)


    if len(residues) == 0:
        ans = 0
    elif len(residues) == 1:
        ans = residues[0] % mod_list[0]
    else:
        ans = crt_all(residues, mod_list)
    print(ans)

