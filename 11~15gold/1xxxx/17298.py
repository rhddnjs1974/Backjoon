import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

stack = []
ans = [-1]*n

for i in range(n):
    if stack:
        while(stack and stack[-1][1]<arr[i]):
            a,b = stack.pop()
            ans[a] = arr[i]
    stack.append((i,arr[i]))

print(*ans)