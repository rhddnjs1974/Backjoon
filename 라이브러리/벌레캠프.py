MOD = 1000000007

def mod_pow(x: int, p: int, mod: int = MOD) -> int:
    x %= mod
    res = 1
    while p:
        if p & 1:
            res = res * x % mod
        x = x * x % mod
        p >>= 1
    return res


def berlekamp_massey(seq: list[int]) -> list[int]:

    ls: list[int] = []
    cur: list[int] = []
    lf = 0
    ld = 1
    for i in range(len(seq)):
        t = 0
        for j in range(len(cur)):
            t = (t + seq[i - j - 1] * cur[j]) % MOD
        if (t - seq[i]) % MOD == 0:
            continue
        if not cur:
            cur = [0] * (i + 1)
            lf = i
            ld = (t - seq[i]) % MOD
            continue

        k = -(seq[i] - t) * mod_pow(ld, MOD - 2) % MOD

        c = [0] * (i - lf - 1)
        c.append(k)
        for j in ls:
            c.append(-j * k % MOD)

        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))

        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % MOD

        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur[:], i, (t - seq[i]) % MOD
        cur = c
    cur = [x % MOD for x in cur]
    return cur


def get_nth(rec: list[int], dp: list[int], n: int) -> int:

    m = len(rec)
    if m == 0:
        return 0
    s = [0] * m
    t = [0] * m
    s[0] = 1
    if m != 1:
        t[1] = 1
    else:
        t[0] = rec[0]

    def mul(v: list[int], w: list[int]) -> list[int]:
        m = len(v)
        tmp = [0] * (2 * m)

        for j in range(m):
            vj = v[j]
            if vj == 0:
                continue
            for k in range(m):
                tmp[j + k] = (tmp[j + k] + vj * w[k]) % MOD

        for j in range(2 * m - 1, m - 1, -1):
            tj = tmp[j]
            if tj == 0:
                continue
            for k in range(1, m + 1):
                tmp[j - k] = (tmp[j - k] + tj * rec[k - 1]) % MOD
        return tmp[:m]

    nn = n
    while nn:
        if nn & 1:
            s = mul(s, t)
        t = mul(t, t)
        nn >>= 1

    res = 0
    for i in range(m):
        res = (res + s[i] * dp[i]) % MOD
    return res


def guess_nth_term(seq: list[int], n: int) -> int:

    if n < len(seq):
        return seq[n] % MOD
    rec = berlekamp_massey(seq)
    if not rec:
        return 0
    return get_nth(rec, seq, n)


# ---- 행렬 관련 (희소 행렬, 최소다항식, determinant) ----

import random
from typing import List, Tuple


def get_min_poly(n: int, M: List[Tuple[int, int, int]]) -> List[int]:

    rnd1 = []
    rnd2 = []
    rng = random.Random(0x14004)
    for _ in range(n):
        rnd1.append(rng.randrange(1, MOD))
        rnd2.append(rng.randrange(1, MOD))

    gobs = []
    for _ in range(2 * n + 2):
        tmp = 0
        for j in range(n):
            tmp = (tmp + rnd2[j] * rnd1[j]) % MOD
        gobs.append(tmp)

        nxt = [0] * n
        # nxt = A * rnd1
        for x, y, v in M:
            nxt[x] = (nxt[x] + v * rnd1[y]) % MOD
        rnd1 = nxt

    sol = berlekamp_massey(gobs)
    sol.reverse()
    return sol


def det(n: int, M: List[Tuple[int, int, int]]) -> int:

    rng = random.Random(0x14004)
    rnd = [rng.randrange(1, MOD) for _ in range(n)]

    M_scaled = [(x, y, v * rnd[y] % MOD) for (x, y, v) in M]

    poly = get_min_poly(n, M_scaled)
    sol = poly[0] 
    if n % 2 == 0:
        sol = (-sol) % MOD

    for r in rnd:
        sol = sol * mod_pow(r, MOD - 2) % MOD

    return sol


############################################

n = int(input())
arr =[1,1,1,2,2,4,5,10,12,25,33,68,91,190,264,555,780,
 1649,2365,5021,7274,15518,22727,48646,71784,
 154162,229094,493346,737215,1591518,2390072,
 5170896,7798020]
print(berlekamp_massey(arr))
x = guess_nth_term(arr, n)

print(x)

