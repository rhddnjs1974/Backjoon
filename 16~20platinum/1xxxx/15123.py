import sys
input = sys.stdin.readline

INF = 1000000000

n, k = map(int, input().split())
s = input().strip()

if n*k > len(s):
    print(-1)
    exit()

dp = {(0, 0, 0): 0}

for c in s:
    ndp = {}
    for (y, x, b), v in dp.items():
        for t in 'DG':
            ny = y
            if t == 'D':
                nx = min(x+1, n)
            else:
                if x == n:
                    ny = min(y+1, k)
                nx = 0

            if c != t:
                nb = 1
            else:
                nb = 0
            
            
            if b == 0 and nb == 1:
                nv = v+1
            else:
                nv = v

            key = (ny, nx, nb)
            if key not in ndp or nv < ndp[key]:
                ndp[key] = nv
    dp = ndp

ans = INF
for (y, x, b), v in dp.items():
    z = y
    if x == n:
        z += 1
    if z >= k:
        ans = min(ans, v)

if ans == INF:
    print(-1)
else:
    print(ans)