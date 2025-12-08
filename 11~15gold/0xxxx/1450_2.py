import sys
input = sys.stdin.readline
import itertools

n,c = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
n = n//2
arr1 = arr[:n]
arr2 = arr[n:]

mo1 = itertools.combinations(arr1,2)
for x in mo1:
    print(x)
    
    
#진행중 이해하고 패스