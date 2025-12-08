import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dist_array = [[INF]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    dist_array[a][b] = 1


for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])

ans = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist_array[i][j] != INF:
            ans[i][j]=1
            ans[j][i]=1

for i in range(1,n+1):
    an = 0
    for j in range(1,n+1):
        if ans[i][j]==0:
            an+=1
    print(an)