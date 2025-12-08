N,M = map(int,input().split())
arr= list(map(int,input().split()))
from itertools import combinations, permutations

ma = 0
for i in combinations(arr,3):
    if sum(i)<=M:
        ma = max(ma,sum(i))

print(ma)