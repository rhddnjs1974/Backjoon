import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
T = int(input())
for i in range(T):
    M,N,x,y = map(int,input().split())

    i,j = 1,1
    ans=1
    while(i!=x or j!=y):
        i = (i%M)+1
        j = (j%N)+1
        ans+=1
        if ans>M*N:
            break
    if ans>M*N:
        print(-1)
    else:
        print(ans)