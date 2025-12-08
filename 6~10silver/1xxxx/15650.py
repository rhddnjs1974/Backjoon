import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,M = map(int,input().split())

arr = []
for i in range(1,N+1):
    arr.append(i)

for x in permutations(arr,M):
    y = sorted(x)
    x = list(x)

    if x==y:
        print(*x)