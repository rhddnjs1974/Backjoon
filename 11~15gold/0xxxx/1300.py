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

        for i in range(1,N+1):
            get+= min((mid//i),N)



        if get >= target:
            end = mid-1
            ans = mid
        else:
            start = mid+1

    return ans

N = int(input())
k = int(input())

print(int(binary_search(k,1,1e10)))
