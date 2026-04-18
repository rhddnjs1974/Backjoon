# 라이브러리: 기하/CCW.py
import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    return c

def dist2(x1, y1, x2, y2):
    return (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)

def cmp(a, b):
    c = ccw(px, py, a[0], a[1], b[0], b[1])
    if c > 0:
        return -1
    if c < 0:
        return 1
    da = dist2(px, py, a[0], a[1])
    db = dist2(px, py, b[0], b[1])
    if da < db:
        return -1
    if da > db:
        return 1
    return 0

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    pts = []
    for i in range(n):
        pts.append((data[1+2*i], data[2+2*i], i))
    piv = 0
    for i in range(1, n):
        if pts[i][1] < pts[piv][1]:
            piv = i
        elif pts[i][1] == pts[piv][1]:
            if pts[i][0] < pts[piv][0]:
                piv = i
    px = pts[piv][0]
    py = pts[piv][1]
    rest = []
    for i in range(n):
        if i != piv:
            rest.append(pts[i])
    rest.sort(key=cmp_to_key(cmp))
    m = len(rest)
    k = m - 1
    while k > 0:
        cc = ccw(px, py, rest[k-1][0], rest[k-1][1], rest[m-1][0], rest[m-1][1])
        if cc != 0:
            break
        k -= 1
    l, r = k, m - 1
    while l < r:
        rest[l], rest[r] = rest[r], rest[l]
        l += 1
        r -= 1
    print(pts[piv][2], end=" ")
    for i in range(m):
        print(rest[i][2], end=" ")
    print()
