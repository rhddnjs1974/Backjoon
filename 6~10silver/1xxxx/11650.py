import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i,j in arr:
    print(i,j)