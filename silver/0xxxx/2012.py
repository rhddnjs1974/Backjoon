import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
ans = 0

for i in range(n):
    ans += abs(arr[i]-(i+1))
print(ans)