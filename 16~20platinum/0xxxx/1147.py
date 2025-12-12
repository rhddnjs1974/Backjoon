N, M = map(int, input().split())
d = {}

for x in range(-N, N + 1):
    for y in range(-M, M + 1):
        if x==0 and y==0:
            continue
        if x < 0 or (x==0 and y < 0):
            x, y = -x, -y
        k = x * x + y * y
        if k not in d:
            d[k] = []
        d[k].append((x, y))

ans = 0
for vecs in d.values():
    vecs = sorted(set(vecs))

    for i in range(len(vecs)):
        ux, uy = vecs[i]
        for j in range(i + 1, len(vecs)):
            vx, vy = vecs[j]
            if ux * vy - uy * vx == 0:
                continue
            
            w = max(0, ux, vx, ux + vx) - min(0, ux, vx, ux + vx)
            h = max(0, uy, vy, uy + vy) - min(0, uy, vy, uy + vy)
            
            if w<=N and h<=M:
                ans += (N-w+1) * (M-h+1)

print(ans)
