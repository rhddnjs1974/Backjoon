import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################


N = int(input())
arr = list(map(int,input().split()))
arr.sort()

M = int(input())
target_arr = list(map(int,input().split()))

for i in target_arr:
    print(bisect_right(arr,i)-bisect_left(arr,i),end=" ")