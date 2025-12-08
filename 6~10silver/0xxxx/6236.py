import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    ans = int(1e9)
    while(start<=end):
        mid = (start+end)//2

        get = 0
        now = 0
        for i in arr:
            if i>mid:
                get=1e9
                break
            if now<i:
                get+=1
                now = mid
            now -= i


        if get <= target:
            end = mid-1
            ans = mid
        else:
            start = mid+1
    return ans

N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))


print(binary_search(M,0,int(1e9)))