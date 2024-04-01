import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
import math

N = int(input())
n = N//2
dp=[0]*15

dp[1] = 1
for i in range(2,15):
    dp[i] = dp[i-1] * (2*i-1)

print(dp[n])