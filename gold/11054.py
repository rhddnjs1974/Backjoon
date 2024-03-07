import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################



N = int(input())
A = list(map(int,input().split()))
LIS = [0]

dp1 = [0] * (N)
dp2 = [0] * (N)

X= -1
for i in A:
    X+=1
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i
    dp1[X] = len(LIS)-1


B =A.reverse()
LIS2 = [0]
X=-1
for i in A:
    X+=1
    point = bisect_left(LIS2,i)
    if point == len(LIS2):
        LIS2.append(i)
    else:
        LIS2[point] = i
    dp2[X] = len(LIS2)-1

dp2.reverse()
ans = 0
for i in range(N):
    ans = max(ans,dp1[i]+dp2[i])
print(ans-1)