import sys, math
input = sys.stdin.readline

N, A = map(int, input().split())
arr = []
for _ in range(N):
    x, y, w = map(int, input().split())
    arr.append((math.sqrt(x * x + y * y), w))
arr.sort()

d = [0] * N
w = [0] * N
for i in range(N):
    d[i] = arr[i][0]
    w[i] = arr[i][1]

W = 0
S = 0
best = 0

for k in range(N+1):
    if k == 0:
        left = 0
    else:
        left = d[k-1]

    if k < N:
        right = d[k]
    else:
        right = -1

    if W > 0:
        r0 = W / (2 * A)
    else:
        r0 = 0

    if k < N:
        if r0 < left:
            r = left
        elif r0>right:
            r = right
        else:
            r = r0
    else:
        if r0 < left:
            r = left
        else:
            r = r0

    best = max(best,(-A)*r*r + W*r - S)

    if k < N:
        W += w[k]
        S += (w[k] * d[k])

print(best)