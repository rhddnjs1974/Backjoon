arr = []
for i in range(int(input())):
    a,b = map(int,input().split())
    arr.append((a,b))
k = int(input())
arr.sort()

ans=0
stack = []
for i in range(len(arr)):
    for x in range(len(stack)-1,-1,-1):
        if stack[x][1]<=arr[i][0]:
            del stack[x]
    stack.append(arr[i])

    ans = max(ans,len(stack))

if ans<=k:
    print(1)
else:
    print(0)