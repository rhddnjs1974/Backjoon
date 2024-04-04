import sys
input = sys.stdin.readline

N,M = map(int,input().split())

m = list(map(int,input().split()))
c = list(map(int,input().split()))

dp = [0]*10001

for a in range(N):
    memo = m[a]
    cost = c[a]
    for i in range(10000,-1,-1):
        if i-cost<0:
            break
        dp[i]= max(dp[i],dp[i-cost]+memo)


for i in range(10001):
    if dp[i]>=M:
        print(i)
        break