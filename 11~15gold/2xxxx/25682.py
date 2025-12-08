import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr =[[]]
Barr = [[0]*(m+1) for i in range(n+1)]
Warr = [[0]*(m+1) for i in range(n+1)]
preBarr = [[0]*(m+1) for i in range(n+1)]
preWarr = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    arr.append(" "+input().rstrip())



for i in range(1,n+1):
    for j in range(1,m+1):
        if (i+j)%2==0:
            if arr[i][j]=="B":
                Barr[i][j]=1
            else:
                Warr[i][j]=1
        else:
            if arr[i][j]=="W":
                Barr[i][j]=1
            else:
                Warr[i][j]=1

for i in range(1,n+1):
    for j in range(1,m+1):
        preBarr[i][j] = preBarr[i-1][j] + preBarr[i][j-1] - preBarr[i-1][j-1] + Barr[i][j]
        preWarr[i][j] = preWarr[i-1][j] + preWarr[i][j-1] - preWarr[i-1][j-1] + Warr[i][j]
        
mi = 1e9
for i in range(k,n+1):
    for j in range(k,m+1):
        mi = min(mi,preBarr[i][j]-preBarr[i-k][j]-preBarr[i][j-k]+preBarr[i-k][j-k])
        mi = min(mi,preWarr[i][j]-preWarr[i-k][j]-preWarr[i][j-k]+preWarr[i-k][j-k])
print(mi)