import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(sum(B),sum(A))