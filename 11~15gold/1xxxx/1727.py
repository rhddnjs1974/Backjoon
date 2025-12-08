n, m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
arr2.sort()

if n<m:
    x = arr1
    y = arr2
else:
    x = arr2
    y = arr1
# x가 더 짧은 배열
n,m = min(n,m),max(n,m)

dp = [[0]*m for i in range(n)]

for i in range(m):
    dp[0][i] = abs(x[0]-y[i])

for i in range(1,n):
    k = dp[i-1][i-1]
    for j in range(i,m):
        k = min(k,dp[i-1][j-1])
        dp[i][j] = k+ abs(x[i]-y[j])

print(min(dp[n-1][n-1:]))