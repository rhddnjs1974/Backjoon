import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

dist_array = [[INF]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    dist_array[a][b] = 1
    dist_array[b][a] = 1

for i in range(1,n+1):
    dist_array[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist_array[i][j] = min(dist_array[i][j],dist_array[i][k]+dist_array[k][j])

mi = 1e9
for i in range(1,n+1):
    s = sum(dist_array[i][1:])

    if s<mi:
        mi = s
        ans = i
print(ans)