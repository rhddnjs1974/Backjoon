import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N,M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

ans = []

def bt(ans,m):
    global M
    if m==M:
        print(*ans)
        return

    for i in arr:
        if len(ans)==0 or i > ans[-1]:
            ans.append(i)
            bt(ans,m+1)
            ans.pop()

bt(ans,0)