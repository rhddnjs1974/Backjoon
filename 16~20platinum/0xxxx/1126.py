k = 500000

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [[-1]*(k+1) for i in range(n)]


for i in range(n):
    t = arr[i]
    dp[i][t] = t
    for j in range(k+1):
        dp[i][j] = max(dp[i][j],dp[i-1][j])
        if j+t<=k and dp[i-1][j]!=-1:
            dp[i][j+t] = max(dp[i][j+t],dp[i-1][j]+t)
        if j>=t and dp[i-1][j]!=-1:
            dp[i][j-t] = max(dp[i][j-t],dp[i-1][j])
        elif j<t and dp[i-1][j]!=-1:
            dp[i][t-j] = max(dp[i][t-j],dp[i-1][j]+t-j)

if n==1:
    print(-1)
else:
    print(dp[n-1][0])
