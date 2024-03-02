import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N = int(input())
P = list(map(int,input().split()))

dp = [1e9]*(2001)
dp[0] = 0

for i in range(N+1):
    for j in range(1,N+1):
        dp[i+j] = min(dp[i+j],dp[i]+P[j-1])

print(dp[N])