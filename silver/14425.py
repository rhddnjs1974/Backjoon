import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = set()
arr2 = []
for i in range(N):
    arr.add(input().rstrip())
for i in range(M):
    x = input().rstrip()
    if x in arr:
        arr2.append(x)

arr2.sort()
print(len(arr2))
