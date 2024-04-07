################희소배열 활용**
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 17 #2**17 = 131072
def tree(node,p,depth):
    dep[node] = depth
    for i,j in graph[node]:
        if i!=p:
            parent[i][0][0] = node
            parent[i][0][1] = j
            tree(i,node,depth+1)

N = int(input())
graph = [[] for i in range(N+1)]
dep = [0] * (N+1)
parent = [[[0,0] for i in range(LOG)] for j in range(N+1)]
for j in range(N-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))


tree(1,0,0)


## 희소배열
for i in range(1,LOG):
    for j in range(1,N+1):
        parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
        parent[j][i][1] = parent[j][i - 1][1] + parent[parent[j][i - 1][0]][i - 1][1]

m = int(input())


for a in range(m):
    k,*arr = map(int,input().split())

    ans = 0
    ans2 = 0

    distx = 1
    disty = 1

    x = arr[0]
    y = arr[1]
    xx = x
    yy = y
    flag = 1

    if dep[x] > dep[y]:
        x,y = y,x
        flag = 2

    for j in range(LOG-1,-1,-1):
        if dep[y] - dep[x] >= 2**j:
            ans += parent[y][j][1]
            y = parent[y][j][0]
            disty+= 2**j

    if x==y:
        if k==1:
            print(ans)
            continue
        else:
            distx-=1
            disty-=1

    for i in range(LOG-1,-1,-1):
        if parent[x][i][0] != parent[y][i][0]:
            distx+= 2**i
            disty+= 2**i
            ans += parent[x][i][1]
            ans += parent[y][i][1]
            x = parent[x][i][0]
            y = parent[y][i][0]

    ans += parent[x][0][1]
    ans += parent[y][0][1]

    if k==1:
        print(ans)
    else:
        if flag==2:
            distx,disty = disty,distx
        dist = arr[2]-1
        if dist<=distx:
            for i in range(LOG - 1, -1, -1):
                if dist >= 2**i:
                    dist-=2**i
                    xx =parent[xx][i][0]
            print(xx)
        else:
            dist = distx+disty-dist
            for i in range(LOG - 1, -1, -1):
                if dist >= 2**i:
                    dist-=2**i
                    yy =parent[yy][i][0]
            print(yy)