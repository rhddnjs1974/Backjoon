import sys
input = sys.stdin.readline


n, k = map(int,input().split())

arr = [i for i in range(0,n+1)]

if n==k:
    print("Impossible")
    exit(0)

arr2 = arr[:n-k+1]

for i in range(2,n-k+1):
    arr[i-1] = arr2[i]

arr[n-k] = 1

print(*arr[1:])