import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    ans = 0
    while(start<=end):
        mid = (start+end)//2

        get = 0
        for i in arr:
            if mid==0:
                get = target+1
            else:
                get += (i//mid)

        if get >= target:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    return ans

K,N = map(int,input().split())
arr = []
for i in range(K):
    arr.append(int(input()))
ma = max(arr)

print(binary_search(N,0,ma))
