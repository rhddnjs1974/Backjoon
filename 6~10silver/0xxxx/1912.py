n = int(input())
arr = list(map(int,input().split()))
dp = [-1e9]*(n+1)

for i in range(n):
    dp[i] = max(arr[i],dp[i-1]+arr[i])
print(max(dp))