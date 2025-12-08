import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

stack = []
dic = {}
ans = [-1]*n

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1


for i in range(n):
    if stack:

        while(stack and dic[stack[-1][1]]<dic[arr[i]]):
            a,b = stack.pop()
            ans[a] = arr[i]
    stack.append((i,arr[i]))

print(*ans)