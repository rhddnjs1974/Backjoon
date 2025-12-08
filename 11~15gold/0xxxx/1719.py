import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
dist_array = [[INF]*(n+1) for i in range(n+1)]

route = [[[] for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    dist_array[a][b] = min(dist_array[a][b],c)
    dist_array[b][a] = min(dist_array[b][a], c)
    route[a][b] = [a, b]
    route[b][a] = [b, a]

for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist_array[i][j] > dist_array[i][k]+dist_array[k][j]:
                dist_array[i][j] = dist_array[i][k]+dist_array[k][j]
                route[i][j] = []
                for x in route[i][k]:
                    route[i][j].append(x)
                for x in route[k][j][1:]:
                    route[i][j].append(x)

for i in range(1,n+1):
    for j in range(1,n+1):
        if len(route[i][j])<=1:
            print("-",end=" ")
        else:
            print(route[i][j][1],end=" ")
    print()