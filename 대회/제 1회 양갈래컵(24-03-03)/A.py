import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

W = int(input())

x = int(2*W)
y = x**0.5

print(int(y)*4)