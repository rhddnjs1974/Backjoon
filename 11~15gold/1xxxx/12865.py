N,K = map(int,input().split())

arr=[]
dp = [1e6] * (200001)
dp[0] = 0

for i in range(N):
    W,V = map(int,input().split())
    for i in range(100001,-1,-1):
        if i-V<0:
            break
        dp[i] = min(dp[i],dp[i-V]+W)

ma = 0


for i in range(100001):
    if dp[i]<=K:
        ma = i
print(ma)