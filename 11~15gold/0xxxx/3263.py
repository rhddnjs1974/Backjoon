import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [[] for i in range(n+2)]
dp = [0]*(n+2)
for i in range(k):
    p,t = map(int,input().split())
    arr[p].append(t)

for i in range(n,0,-1):
    if len(arr[i])==0:
        dp[i] = dp[i+1]+1
    else:
        for j in arr[i]:
            if i+j<=n+1:
                dp[i] = max(dp[i],dp[i+j])

print(dp[1])
    