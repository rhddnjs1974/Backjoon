import sys
input = sys.stdin.readline
from itertools import combinations, permutations


arr = []
for i in range(9):
    arr.append(int(input()))

for x in combinations(arr,7):
    if sum(x)==100:
        x = list(x)
        x.sort()
        for a in x:
            print(a)
        break