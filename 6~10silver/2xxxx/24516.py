import sys
input = sys.stdin.readline

N = int(input())

arr = []
x = -1
for i in range(N):
    x+=2
    arr.append(x)

print(*arr)