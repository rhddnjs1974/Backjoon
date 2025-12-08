import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr =[]
for i in range(n):
    t = int(input())
    if t<=k:
        arr.append(t)

dp = [0]*(k+1)
dp[0] = 1
for a in arr:
    for i in range(k+1):
        if a+i>=k+1:
            break
        dp[a+i]+=dp[i]
print(dp[k])