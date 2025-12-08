import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

index1 = [0]*(n+1)
for i in range(n):
    index1[A[i]] = i
    
for i in range(n):
    B[i] = index1[B[i]]

LIS = [-1]

for i in B:
    point = bisect_left(LIS,i)
    if point == len(LIS):
        LIS.append(i)
    else:
        LIS[point] = i

print(len(LIS)-1)
