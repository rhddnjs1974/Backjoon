import sys
import math
from functools import cmp_to_key

input = sys.stdin.readline

def half(v):
    x, y = v
    if y > 0:
        return 0
    if y == 0 and x > 0:
        return 0
    return 1

def cmp_dir(a, b):
    ha = half(a)
    hb = half(b)
    if ha != hb:
        if ha < hb:
            return -1
        else:
            return 1

    ax, ay = a
    bx, by = b
    cross = ax * by - ay * bx
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0

N, Q = map(int, input().split())

dirs = [None] * (N + 1)
cnt = {}

i = 1
while i <= N:
    x, y = map(int, input().split())
    g = math.gcd(abs(x), abs(y))
    dx = x // g
    dy = y // g
    d = (dx, dy)
    dirs[i] = d

    if d in cnt:
        cnt[d] += 1
    else:
        cnt[d] = 1
    i += 1

uniq = list(cnt.keys())
uniq.sort(key=cmp_to_key(cmp_dir))

K = len(uniq)
idx = {}
i = 0
while i < K:
    idx[uniq[i]] = i
    i += 1

pref = [0] * (K + 1)
i = 0
while i < K:
    pref[i + 1] = pref[i] + cnt[uniq[i]]
    i += 1

total = pref[K]

def arc_sum_ccw(l, r):
    if l <= r:
        return pref[r + 1] - pref[l]
    return (total - (pref[l] - pref[r + 1]))

for j in range(Q):
    a, b = map(int, input().split())
    da = dirs[a]
    db = dirs[b]
    ia = idx[da]
    ib = idx[db]

    if ia == ib:
        print(cnt[da])
    else:
        print(arc_sum_ccw(ib, ia))

