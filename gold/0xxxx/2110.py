import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
########################################

def binary_search(target,start,end):
    ans = 0
    global N
    while(start<=end):
        mid = (start+end)//2
        get = 0
        now_point = 0

        while(now_point<N):
            now = arr[now_point]
            now_point = bisect_left(arr, now + mid)
            get+=1

        if get >= target:
            start = mid+1
            ans = mid
        else:
            end = mid-1

    return ans

N,C = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

print(int(binary_search(C,1,1e9)))
