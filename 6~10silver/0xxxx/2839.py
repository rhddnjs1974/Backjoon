n = int(input())


dp = [1e9]*5006
dp[0]=0
for i in range(5001):
    dp[i+3] = min(dp[i+3],dp[i]+1)
    dp[i+5] = min(dp[i+5],dp[i]+1)

if dp[n]!=1e9:
    print(dp[n])
else:
    print(-1)