import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

e,s,m = map(int,input().split())

E,S,M = 1,1,1
ans=1
while(E!=e or s!=S or M!=m):
    ans+=1
    E = (E%15)+1
    S = (S % 28) + 1
    M = (M % 19) + 1

print(ans)