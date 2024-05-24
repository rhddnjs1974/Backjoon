import sys
input = sys.stdin.readline

n,l,r = map(int,input().split())
dp = [[[0]*(n+1) for i in range(n+1)] for j in range(n+1)]

dp[1][1][1] = 1

for i in range(2,n+1):
    for j in range(1,i+1):
        for k in range(1,i+1):
            dp[i][j][k] = dp[i-1][j-1][k] + dp[i-1][j][k-1] + dp[i-1][j][k]*(i-2)


print(dp[n][l][r]%1000000007)