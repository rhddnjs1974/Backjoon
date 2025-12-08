import sys
input = sys.stdin.readline
########################################

n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

dp = [[1e9]*n for i in range(n)]
for i in range(n):
    dp[i][i] = 0

for i in range(1,n): # 길이
    for j in range(n):
        if i+j>=n:
            break

        for k in range(j,i+j):

            dp[j][i+j] = min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+arr[j][0]*arr[k][1]*arr[i+j][1])


print(dp[0][n-1])