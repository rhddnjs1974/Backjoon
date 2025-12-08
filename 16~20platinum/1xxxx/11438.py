import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 17 #2**17 = 131072
def tree(node,p,depth):
    parent[node][0] = p
    dep[node] = depth
    for i in graph[node]:
        if i!=p:
            parent[i][0] = node
            tree(i,node,depth+1)

N = int(input())
graph = [[] for i in range(N+1)]
dep = [0] * (N+1)
parent = [[0]*(LOG) for i in range(N+1)]
for j in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


tree(1,0,0)


## 희소배열
for i in range(1,LOG):
    for j in range(1,N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m = int(input())

for i in range(m):
    x,y = map(int,input().split())

    if dep[x] > dep[y]:
        x,y = y,x

    for j in range(LOG-1,-1,-1):
        if dep[y] - dep[x] >= 2**j:
            y = parent[y][j]

    if x==y:
        print(x)
        continue

    for i in range(LOG-1,-1,-1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]

    print(parent[x][0])

