import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

N = int(input())
A = list(map(int,input().split()))
LIS = [-1e8]

for j in A:
    i = -j
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i

print(N-len(LIS)+1)

