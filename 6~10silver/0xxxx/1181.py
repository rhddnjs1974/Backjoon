import sys
input = sys.stdin.readline

n = int(input())
arr=set()
for i in range(n):
    arr.add(input().rstrip())

arr = list(arr)
arr.sort()
arr.sort(key=lambda x : len(x))

for i in arr:
    print(i)