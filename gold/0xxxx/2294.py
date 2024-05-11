import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr =[]
for i in range(n):
    t = int(input())
    if t<=k:
        arr.append(t)

dp = [1e9]*(k+1)
dp[0] = 0
for a in arr:
    for i in range(k+1):
        if a+i>=k+1:
            break
        dp[a+i]=min(dp[a+i],dp[i]+1)

if dp[k]!=1e9:
    print(dp[k])
else:
    print(-1)