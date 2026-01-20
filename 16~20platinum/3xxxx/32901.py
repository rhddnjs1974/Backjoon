import sys
input = sys.stdin.readline

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

n = int(input().strip())
xs = [0] * n
ys = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    xs[i] = x
    ys[i] = y

P2 = 0
for i in range(n):
    j = (i + 1) % n
    P2 += cross(xs[i], ys[i], xs[j], ys[j])

suffx = [0] * (n + 1)
suffy = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffx[i] = suffx[i + 1] + xs[i]
    suffy[i] = suffy[i + 1] + ys[i]

PCS = [0] * (n + 1)
for s in range(n - 2, -1, -1):
    PCS[s] = PCS[s + 1] + cross(xs[s], ys[s], suffx[s + 1], suffy[s + 1])

sumA = 0
for s in range(1, n):
    sumA += PCS[s]

prefx = 0
prefy = 0

B = 0
for j in range(n):
    if 1 <= j <= n - 2:
        w = n - 1 - j
        B += w * cross(prefx, prefy, xs[j], ys[j])
    prefx += xs[j]
    prefy += ys[j]

wx = 0
wy = 0
prefx = 0
prefy = 0
C = 0
for k in range(n):
    if k >= 2:
        px = prefx - xs[k - 1]
        py = prefy - ys[k - 1]
        wpx = wx - (k - 1) * xs[k - 1]
        wpy = wy - (k - 1) * ys[k - 1]

        C += (k - 1) * cross(px, py, xs[k], ys[k]) - cross(wpx, wpy, xs[k], ys[k])

    prefx += xs[k]
    prefy += ys[k]
    wx += k * xs[k]
    wy += k * ys[k]

S = sumA + B - C

print(S / P2)