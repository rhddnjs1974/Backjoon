N = int(input())
dp_r = [1e9]*N
dp_g = [1e9]*N
dp_b = [1e9]*N

for i in range(N):
    r,g,b = map(int,input().split())
    if i==0:
        dp_r[i] = r
        dp_g[i] = g
        dp_b[i] = b
    else:
        dp_r[i] = min(dp_g[i - 1], dp_b[i - 1]) + r
        dp_g[i] = min(dp_r[i - 1], dp_b[i - 1]) + g
        dp_b[i] = min(dp_g[i - 1], dp_r[i - 1]) + b

print(min(dp_r[N-1],dp_g[N-1],dp_b[N-1]))