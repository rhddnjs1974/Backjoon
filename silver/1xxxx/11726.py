import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
dp = [0]*1005
dp[0] = 1
for i in range(1001):
    dp[i+1] += dp[i]
    dp[i+2] += dp[i]

n = int(input())
print(dp[n]%10007)