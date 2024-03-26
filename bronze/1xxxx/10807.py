n = int(input())
arr = list(map(int,input().split()))
v = int(input())

ans = 0
for i in arr:
    if i == v:
        ans+=1

print(ans)