import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    ans = 0
    while(start<=end):
        mid = (start+end)//2
        get = 0
        for i in arr:
            if i>mid:
                get+= mid
            else:
                get+= i

        if get <= target:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    return ans

N = int(input())
arr = list(map(int,input().split()))
ma = max(arr)
M = int(input())

print(binary_search(M,0,ma))
