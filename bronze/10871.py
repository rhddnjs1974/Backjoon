import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,X = map(int,input().split())
arr = list(map(int,input().split()))
for i in arr:
    if i<X:
        print(i,end=" ")