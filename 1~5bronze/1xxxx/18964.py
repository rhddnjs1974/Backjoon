import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

c = 0
for x in arr:
    if x%2==0:
        c += 1

if c >= n-c:
    print(2, 0)
else:
    print(2, 1)