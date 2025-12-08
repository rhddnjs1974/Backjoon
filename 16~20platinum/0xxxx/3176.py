################희소배열 활용**
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 17 #2**17 = 131072
def tree(node,depth):
    visit[node] = 1
    dep[node] = depth
    for i,j in graph[node]:
        if visit[i]==0:
            parent[i][0] = [node,j,j]
            tree(i,depth+1)

N = int(input())
graph = [[] for i in range(N+1)]
dep = [0] * (N+1)
parent = [[[0]*3 for i in range(LOG)] for j in range(N+1)]
visit = [0]*(N+1)
for j in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

tree(1,0)



## 희소배열
for i in range(1,LOG):
    for j in range(1,N+1):
        parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
        parent[j][i][1] = min(parent[j][i-1][1],parent[parent[j][i-1][0]][i-1][1])
        parent[j][i][2] = max(parent[j][i-1][2], parent[parent[j][i-1][0]][i-1][2])

m = int(input())


for i in range(m):
    x,y = map(int,input().split())
    mi = 1e9
    ma = 0

    if dep[x] > dep[y]:
        x,y = y,x

    for j in range(LOG-1,-1,-1):
        if dep[y] - dep[x] >= 2**j:
            mi = min(mi, parent[y][j][1])
            ma = max(ma, parent[y][j][2])
            y = parent[y][j][0]

    if x==y:
        print(mi,ma)
        continue

    for i in range(LOG-1,-1,-1):
        if parent[x][i][0] != parent[y][i][0]:

            mi = min(mi, parent[x][i][1])
            ma = max(ma, parent[x][i][2])

            mi = min(mi, parent[y][i][1])
            ma = max(ma, parent[y][i][2])
            x = parent[x][i][0]
            y = parent[y][i][0]

    mi = min(mi, parent[x][0][1])
    ma = max(ma, parent[x][0][2])
    mi = min(mi, parent[y][0][1])
    ma = max(ma, parent[y][0][2])
    print(mi,ma)

