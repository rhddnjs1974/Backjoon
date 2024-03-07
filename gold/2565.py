import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

N = int(input())
arr = [0]*501
for i in range(N):
    a,b = map(int,input().split())
    arr[a] = b
A = []
for i in arr:
    if i!=0:
        A.append(i)


LIS = [0]

for i in A:
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i

print(N-len(LIS)+1)

