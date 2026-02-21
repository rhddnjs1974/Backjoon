import sys
import math
input = sys.stdin.readline

def primeList(n):
    n+=1
    arr = [0,0] + [1]*n

    for i in range(2,int(n**0.5)+1):
        if arr[i]==1:
            for j in range(i*2,n+1,i):
                arr[j] = 0

    return arr

x = primeList(1000)

n = int(input())
arr= list(map(int,input().split()))
arr.sort()

if n>=3:
    print("YES")
    print(2)
    print(arr[-2],arr[-1])
else:
    if arr[0]==1 and x[arr[1]]==1:
        print("NO")
    else:
        print("YES")
        print(2)
        print(arr[0],arr[1])