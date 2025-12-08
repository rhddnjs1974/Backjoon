N = int(input())
dp_r = [[1e9]*N for i in range(3)]
dp_g = [[1e9]*N for i in range(3)]
dp_b = [[1e9]*N for i in range(3)]
# 0 r 1 g 2 b 시작

for i in range(N):
    r,g,b = map(int,input().split())
    if i==0:
        dp_r[0][i] = r
        dp_g[1][i] = g
        dp_b[2][i] = b
    else:
        for j in range(3):
            dp_r[j][i] = min(dp_g[j][i - 1], dp_b[j][i - 1]) + r
            dp_g[j][i] = min(dp_r[j][i - 1], dp_b[j][i - 1]) + g
            dp_b[j][i] = min(dp_g[j][i - 1], dp_r[j][i - 1]) + b

    if i==N-1:
        dp_r[0][i] = 1e9
        dp_g[1][i] = 1e9
        dp_b[2][i] = 1e9


print(min(dp_r[0][N-1],dp_g[0][N-1],dp_b[0][N-1],dp_r[1][N-1],dp_g[1][N-1],dp_b[1][N-1],dp_r[2][N-1],dp_g[2][N-1],dp_b[2][N-1],))