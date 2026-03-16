N,T =map(int,input().split())

dp = [0]*(T+1)
for i in range(N):
    K,S = map(int,input().split())
    for j in range(T,K-1,-1):
        dp[j] = max(dp[j],dp[j-K]+S)

print(max(dp))