import sys, math
input = sys.stdin.readline

INF = 10**60
EPS = 1e-12

n, h, alpha, beta = map(int, input().split())
x, y = zip(*(map(int, input().split()) for _ in range(n)))
x, y = list(x), list(y)

slope = [(y[k+1]-y[k])/(x[k+1]-x[k]) for k in range(n-1)]

def ground(k, X):
    return y[k] + slope[k]*(X - x[k])

def seg_min_gap(i, j, k):
    xi, xj = x[i], x[j]
    m = (xi + xj)/2
    r = (xj - xi)/2
    cand = []

    for X in (x[k], x[k+1]):
        if X < xi - EPS or X > xj + EPS: continue
        dx = X - m
        if abs(dx) > r + 1e-9: continue
        arch = (h - r) + math.sqrt(max(r*r - dx*dx, 0.0))
        cand.append(arch - ground(k, X))

    s = slope[k]
    c = s / math.sqrt(1 + s*s)
    Xc = m + r * c
    if x[k]-EPS <= Xc <= x[k+1]+EPS:
        dx = Xc - m
        arch = (h - r) + math.sqrt(max(r*r - dx*dx, 0.0))
        cand.append(arch - ground(k, Xc))

    return min(cand) if cand else INF

def extend_right(i):
    j = i + 1
    while j < n:
        ok = True
        xi, xj = x[i], x[j]
        if seg_min_gap(i, j, j-1) < -1e-9:
            ok = False
        if not ok:
            break
        j += 1
    return j - 1


right_limit = [i for i in range(n)]
for i in range(n-1):
    right_limit[i] = extend_right(i)

dp = [INF]*n
dp[0] = (h - y[0]) * alpha

for i in range(n):
    if dp[i] >= INF: 
        continue
    for j in range(i+1, right_limit[i]+1):
        dx = x[j] - x[i]
        cost = alpha*(h - y[j]) + beta*(dx*dx)
        dp[j] = min(dp[j], dp[i] + cost)

if dp[-1]>=INF/2:
    print("impossible")
else:
    print(int(dp[-1]))
