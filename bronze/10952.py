import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################


while(True):
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)