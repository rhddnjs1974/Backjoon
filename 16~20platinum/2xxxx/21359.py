import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = []
for _ in range(N):
    s.append(input().strip())

arr = []
for i in range(N):
    h = 0
    for j in range(M):
        if s[i][j] == '.':
            h |= (1 << j)
    g = [0] * (1 << M)
    for r in range(M):
        if r == 0:
            rot = h
        else:
            rot = ((h << r) | (h >> (M-r))) & ((1 << M)-1)
        sub = rot
        while True:
            g[sub] += 1
            if sub == 0:
                break
            sub = (sub-1) & rot
    arr.append(g)

ans = 0
for S in range(1, 1 << M):
    x = 1
    for i in range(N):
        x *= arr[i][S]
        if x == 0:
            break
    if S.bit_count()%2==1:
        ans += x
    else:
        ans -= x

print(ans)