import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,S = input().split()
N = int(N)

ans = 0
for i in range(N):
    x,y = input().split()
    y = int(y)
    x = list(x.split("_"))
    for j in x:
        if j==S:
            ans+=y
            break

print(ans)