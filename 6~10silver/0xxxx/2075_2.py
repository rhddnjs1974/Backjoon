import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x = list(map(int,input().split()))
    for a in x:
        arr.append(a)

arr.sort()
print(arr[-5])