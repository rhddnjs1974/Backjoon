import sys
input = sys.stdin.readline

N, K = map(int,input().split())
MOD = 10**9

dp = [0] * (max(N,K) + 1)
window = 0

for i in range(K):
    dp[i] = 1
    window += dp[i]

for i in range(K, N + 1):
    dp[i] = window % MOD
    window += dp[i]
    window -= dp[i - K]

print(dp[N] % MOD)