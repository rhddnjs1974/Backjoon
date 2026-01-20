import sys
input = sys.stdin.readline

def range_sum(pref, l, r):
    return pref[r] - pref[l - 1]

def S(P, r):
    P2 = P + N
    return range_sum(pcw, P2 - r, P2) + range_sum(pccw, P2, P2 + r)

def C(P, T):
    k = T // N
    r = T - k * N
    return k * M + S(P, r)

N, M, Q = map(int, input().split())

cw = [0] * (N + 1)
ccw = [0] * (N + 1)

for i in range(M):
    p, d = map(int, input().split())
    if d == 0:
        cw[p] = 1
    else:
        ccw[p] = 1

L = 3 * N
pcw = [0] * (L + 1)
pccw = [0] * (L + 1)

for i in range(1, L + 1):
    x = (i - 1) % N + 1
    pcw[i] = pcw[i - 1] + cw[x]
    pccw[i] = pccw[i - 1] + ccw[x]

for i in range(Q):
    P, X = map(int, input().split())

    kmax = (X + M - 1) // M - 1
    hi = kmax * N + (N - 1)
    lo = 0

    while lo < hi:
        mid = (lo + hi) // 2
        if C(P, mid) >= X:
            hi = mid
        else:
            lo = mid + 1

    print(lo)

