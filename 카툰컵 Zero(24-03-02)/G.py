import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,Q = map(int,input().split())
D = list(map(int,input().split()))

ans = [0]*N

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if D[i] > D[j]:
            dp[i] = max(dp[i], dp[j] + 1)

dp2 = [1 for i in range(N)]

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if D[i] < D[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)


for i in range(Q):
    x = int(input())-1
    print(dp[x]+dp2[x]-1)

