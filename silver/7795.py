import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################


T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr2.sort()

    ans=0
    for i in arr:
        ans += bisect_left(arr2,i)
    print(ans)