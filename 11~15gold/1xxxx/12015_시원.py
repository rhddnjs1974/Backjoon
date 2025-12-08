import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(arr,q,i,j):
    if i>=j:
        return j
    x = (i+j)//2
    if arr[x] >q:
        return bin(arr,q,i,x)
    else:
        return bin(arr,q,x+1,j)

def bin2(i,j):
    if i>=j:
        if i > n:
            return n
        else:
            return j-1

    x = (i+j)//2
    arr = [100000000 for i in range(x)]
    for q in k:
        p = bin(arr,q,0,len(arr))
        if len(arr) <= p:
            continue
        if arr[p] ==100000000 or arr[p] > q:
            if p==0:
                arr[p] = q
            else:
                if arr[p-1] < q:
                    arr[p] = q

    if 100000000 in arr:
        return bin2(i,x)
    else:
        return bin2(x+1,j)

n = int(input())
k = list(map(int, input().split()))
print(bin2(0,len(k)))