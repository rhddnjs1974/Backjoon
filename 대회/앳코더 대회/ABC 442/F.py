import sys
input = sys.stdin.readline

n = int(input())
arr= []

for i in range(n):
    x = input()
    arr.append(x)
    
prefix = []

for i in range(n):
    prefix.append([0])
    for j in range(n):
        if arr[i][j]=="#":
            prefix[-1].append(prefix[-1][-1]+1)
        else:
            prefix[-1].append(prefix[-1][-1])

dp = [[]]
dp2 = [[0]*(n+1)] # 그 행 뒤에서부터 최소값 용

for i in range(n+1):
    dp[0].append(n-i-prefix[0][n]+2*prefix[0][i])

dp2[0][n] = dp[0][n]
for i in range(n-1,-1,-1):
    dp2[0][i] = min(dp2[0][i+1],dp[0][i])

for i in range(1,n):
    dp.append([0]*(n+1))
    dp2.append([0]*(n+1))
    for j in range(n+1):
        dp[i][j] = n-j-prefix[i][n]+2*prefix[i][j]
        dp[i][j] += dp2[i-1][j]
        
    dp2[i][n] = dp[i][n]
    for j in range(n-1,-1,-1):
        dp2[i][j] = min(dp2[i][j+1],dp[i][j])

print(min(dp[-1]))