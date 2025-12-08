import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arrP = [0]*(n+1)
flag = 0
for i in arr:
    if i==-1:
        continue
    if i<0 or i>n:
        flag=1
        break
    arrP[i] += 1
    if arrP[i]!=1:
        flag=1
        break
    
if flag==1:
    print("No")
else:
    print("Yes")
    arrx = []
    for i in range(1,n+1):
        if arrP[i]==0:
            arrx.append(i)
    
    t=0
    ans = []
    for i in arr:
        if i==-1:
            ans.append(arrx[t])
            t+=1
        else:
            ans.append(i)
    print(*ans)