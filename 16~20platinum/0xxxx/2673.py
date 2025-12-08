n = int(input())
dp = [[0]*101 for i in range(101)]
arr = [[0]*101 for i in range(101)]
for i in range(n):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
     
for i in range(1,101):
    for j in range(i,0,-1):
        for k in range(j,i):
            dp[j][i] = max(dp[j][i], dp[j][k]+dp[k][i]+arr[j][i])

print(dp[1][100])