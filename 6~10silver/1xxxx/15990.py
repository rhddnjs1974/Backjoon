import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

dp1=[0]*100004
dp2=[0]*100004
dp3=[0]*100004
dp1[1] = 1
dp2[2] = 1
dp3[3] = 1

for i in range(100001):
    dp2[i + 2] += (dp1[i]+ dp3[i])%1000000009
    dp3[i + 3] += (dp1[i]+ dp2[i])%1000000009
    dp1[i + 1] += (dp2[i]+ dp3[i])%1000000009


T = int(input())
for i in range(T):
    N = int(input())
    print((dp1[N]+dp2[N]+dp3[N])%1000000009)


