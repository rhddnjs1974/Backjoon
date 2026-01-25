import sys
import bisect
input = sys.stdin.readline

w1 = []
w2 = []
w3 = []

n, C = map(int, input().split())
for _ in range(n):
    w, v, k = map(int, input().split())
    if w == 1:
        w1.append((v, k))
    elif w == 2:
        w2.append((v, k))
    else:
        w3.append((v, k))

w1.sort(reverse=True)
w2.sort(reverse=True)
w3.sort(reverse=True)

def build(group):
    m = len(group)
    cnt = [0] * (m + 1)
    s = [0] * (m + 1)

    for i in range(m):
        v, k = group[i]
        cnt[i + 1] = cnt[i] + k
        s[i + 1] = s[i] + v * k

    return cnt, s, group

c1, s1, g1 = build(w1)
c2, s2, g2 = build(w2)
c3, s3, g3 = build(w3)

A = c1[-1]
B = c2[-1]
D = c3[-1]

def sum_top(cnt, sm, grp, t):
    if t <= 0:
        return 0
    if t >= cnt[-1]:
        return sm[-1]
    i = bisect.bisect_left(cnt, t)

    base = sm[i - 1]
    used = cnt[i - 1]
    v, k = grp[i - 1]
    return base + (t - used) * v

def kth_val(cnt, grp, t):
    if t <= 0 or t > cnt[-1]:
        return None
    i = bisect.bisect_left(cnt, t)
    v, k = grp[i - 1]
    return v

def best12(R):
    if R <= 0:
        return 0

    ymax = R // 2
    if ymax > B:
        ymax = B

    def f(y):
        x = R - 2 * y
        if x > A:
            x = A
        return sum_top(c2, s2, g2, y) + sum_top(c1, s1, g1, x)

    l = 0
    r = ymax
    while r - l > 10:
        m1 = (2 * l + r) // 3
        m2 = (l + 2 * r) // 3
        if f(m1) < f(m2):
            l = m1
        else:
            r = m2

    best = 0
    y = l
    while y <= r:
        val = f(y)
        if val > best:
            best = val
        y += 1
    return best

def total_value(z):
    if z < 0:
        return -1
    if z > D:
        return -1
    R = C - 3 * z
    if R < 0:
        return -1
    return sum_top(c3, s3, g3, z) + best12(R)

Zmax = C // 3
if Zmax > D:
    Zmax = D

l = 0
r = Zmax
while r - l > 10:
    m1 = (2 * l + r) // 3
    m2 = (l + 2 * r) // 3
    if total_value(m1) < total_value(m2):
        l = m1
    else:
        r = m2

ans = 0
z = l
while z <= r:
    val = total_value(z)
    if val > ans:
        ans = val
    z += 1

print(ans)
