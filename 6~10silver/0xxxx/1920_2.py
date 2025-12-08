import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
arr.sort()
arr.append(1e12)
for i in arr2:
    t = bisect.bisect_left(arr,i)
    if arr[t]==i:
        print(1)
    else:
        print(0)