import sys
input = sys.stdin.readline

def feasible(points, L, k):
    pts = sorted(points)
    n = len(pts)
    eps = 1e-12

    j = 0
    for i in range(n):
        x0 = pts[i][0]
        if j < i:
            j = i
        while j < n and pts[j][0] <= x0 + L + eps:
            j += 1

        m = j - i
        if m < k:
            continue

        ys = []
        for t in range(i,j):
            ys.append(pts[t][1])
        ys.sort()

        a = 0
        for b in range(m):
            while ys[b] - ys[a] > L + eps:
                a += 1
            if b - a + 1 >= k:
                return True, x0, ys[a]

    return False, 0.0, 0.0

def check(points, L, k):
    ok, x0, y0 = feasible(points, L, k)
    if ok:
        return True, x0, y0

    mirrored = [(-x, y) for x, y in points]
    ok, xm, ym = feasible(mirrored, L, k)
    if ok:
        return True, -xm - L, ym

    return False, 0.0, 0.0

n = int(input())
points = []
for i in range(n):
    x,y = map(float,input().split())
    points.append((x,y))
k = (n + 1) // 2

xs = []
ys = []
for p in points:
    xs.append(p[0])
    ys.append(p[1])

hi = 100015
lo = 0.0

ans1 = points[0][0]
ans2 = points[0][1]

for _ in range(100):
    mid = (lo + hi) / 2.0
    ok, x0, y0 = check(points, mid, k)
    if ok:
        hi = mid
        ans1, ans2 = x0, y0
    else:
        lo = mid

print(hi)
print(ans1,ans2)
