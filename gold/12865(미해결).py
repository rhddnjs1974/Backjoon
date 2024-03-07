N,K = map(int,input().split())

arr=[]
dp = [1e5] * (200001)

for i in range(N):
    W,V = map(int,input().split())
    dp[V] = min(dp[V],W)
    for i in range(100001):
        dp[i+V] = min(dp[i+V],dp[i]+W)

ma = 0
for i in range(100001):
    if dp[i]<=K:
        ma = i
print(ma)