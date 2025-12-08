import sys
input = sys.stdin.readline
from itertools import combinations, permutations
INF = int(1e9)

n,m = map(int,input().split())
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

hubo = []
for i in range(1,n+1):
    hubo.append(i)

mi = 1e9
for x,y in combinations(hubo, 2):
    mi = min(dist_array[x][y]+dist_array[y][x],mi)

if mi==1e9:
    print(-1)
else:
    print(mi)