n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

ans = [1]*n
for i in range(n):
    for j in range(n):
        if arr[j][0]>arr[i][0] and arr[j][1]>arr[i][1]:
            ans[i]+=1

print(*ans)