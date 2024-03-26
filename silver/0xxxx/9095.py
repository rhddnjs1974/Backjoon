import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

dp = [0]*14
dp[0] = 1
for i in range(11):
    dp[i+1] += dp[i]
    dp[i+2] += dp[i]
    dp[i+3] += dp[i]

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])