n = int(input())
arr = [[0]*n for i in range(n)]

for i in range(n):
    arr2 = list(map(int,input().split()))
    for j in range(i+1):
        arr[i][j] = arr2[j]

dp = [[0]*n for i in range(n)]
for i in range(n):
    if i == 0:
        dp[0][0] = arr[0][0]
    else:
        for j in range(i+1):
            if j==0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))