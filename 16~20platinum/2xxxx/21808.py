import sys
input = sys.stdin.readline

n = int(input())
d = [0]+list(map(int, input().split()))

dp = [None]*(n+1)
dp[1] = [0]
for i in range(2, n+1):
    dp[i] = [0]*i

for j in range(1, n):
    best = [0]*(j+1)
    for k in range(1, j+1):
        best[k] = best[k-1]
        if dp[j][k-1] > best[k]:
            best[k] = dp[j][k-1]

    pos = []
    val = []

    l = j
    r = j+1
    sl = d[l]
    sr = d[r]
    add = 0

    while True:
        if sl == sr:
            if l >= 2 and r <= n-1:
                add += 1
                pos.append(r+1)
                val.append(best[l-1]+add)
                l -= 1
                r += 1
                sl += d[l]
                sr += d[r]
            else:
                break
        elif sl < sr:
            if l == 1:
                break
            l -= 1
            sl += d[l]
        else:
            if r == n:
                break
            r += 1
            sr += d[r]

    p = 0
    now = best[j]
    m = len(pos)

    for i in range(j+1, n+1):
        while p < m and pos[p] == i:
            if val[p] > now:
                now = val[p]
            p += 1
        dp[i][j] = now

ans = 0
for x in dp[n]:
    if x > ans:
        ans = x

print(ans)