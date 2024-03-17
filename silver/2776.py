import sys
input = sys.stdin.readline
########################################

def binary_search(target,start,end):
    while(start<=end):
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()


    M = int(input())
    target_arr = list(map(int,input().split()))

    for i in target_arr:
        if binary_search(i,0,N-1)==None:
            print(0)
        else:
            print(1)