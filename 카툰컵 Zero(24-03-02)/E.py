import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,M = map(int,input().split())

n=1
for i in range(2,N+1):
    n = (n*i)%M

print(n)