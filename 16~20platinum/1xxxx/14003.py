import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

N = int(input())
A = list(map(int,input().split()))
LIS = [-1e10]
INDEX = []
for i in A:
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i
    INDEX.append(point)



print(len(LIS)-1)


ans=[]
now = len(LIS)-1
for i in range(N-1,-1,-1):
    if INDEX[i]==now:
        ans.append(A[i])
        now-=1
ans.reverse()
print(*ans)