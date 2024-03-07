import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

N = int(input())
A = list(map(int,input().split()))
LIS = [-1001]

for i in A:
    i = -i
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i

print(len(LIS)-1)

