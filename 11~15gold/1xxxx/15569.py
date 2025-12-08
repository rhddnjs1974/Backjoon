import sys
input = sys.stdin.readline
MOD = 1999

N, M = map(int, input().split())

W = max(N, M)

dp = [[0] * (W+1) for i in range(N+1)]

dp[0][N] = 1 
dp[1][N] = 1
dp[N][1] = 1

for i in range(2, N + 1):
    s = 0
    for j in range(1, i + 1):
        s += dp[i - j][N]
    dp[i][N] = s
    dp[N][i] = dp[i][N]

b = (dp[N][N] - 1)

dp[N][N] = ((dp[N][N] * 2) - 1)

for i in range(N+1,M+1):
    now = 0
    for j in range(1,N+1):
        if j == N:
            now += dp[N][i-j] * (1+b)
        else:
            now += dp[N][i-j]
    dp[N][i] = now

print(dp[N][M] % MOD)

