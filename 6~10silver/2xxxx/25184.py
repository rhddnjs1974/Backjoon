import sys
n = int(input())

ans=[]
for i in range(n//2,0,-1):
    t = i
    while(t<=n):
        ans.append(t)
        t+=(n//2)


if n==1:
    print(1)
else:
    print(*ans)