import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    ans = 1e9
    while(start<=end):
        mid = (start+end)//2

        get = 0
        made = 0
        for i in range(N):
            if arr[i]>mid:
                made = 1e9
                break
            if get+arr[i]<=mid:
                get+=arr[i]
            else:
                get = arr[i]
                made+=1


        if made < target:
            end = mid-1
            ans = mid

        else:
            start = mid+1
    return ans

N,M = map(int,input().split())
arr = list(map(int,input().split()))



print(binary_search(M,0,int(1e9)))
