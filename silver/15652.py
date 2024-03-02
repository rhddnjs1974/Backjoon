import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,M = map(int,input().split())

arr = []
for i in range(1,N+1):
    arr.append(i)

ans = []

def bt(ans,m):
    global M
    if m==M:
        print(*ans)
        return

    if len(ans)==0:
        t = 1
    else:
        t = ans[-1]

    for i in range(t,N+1):
        ans.append(i)
        bt(ans,m+1)
        ans.pop()

bt(ans,0)