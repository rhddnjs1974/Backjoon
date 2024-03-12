import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dist_array = [[INF]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    dist_array[a][b] = min(dist_array[a][b],c)

for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist_array[i][j] == INF:
            print(0,end=" ")
        else:
            print(dist_array[i][j],end=" ")
    print()