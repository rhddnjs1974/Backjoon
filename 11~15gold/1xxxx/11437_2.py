import sys
input = sys.stdin.readline

log = 16

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0]*(n+1)
parent = [[0]*log for i in range(n+1)]
q = [1]
dep = [0]*(n+1)
dep[1] = 1

while(q):
    x = q.pop()
    visit[x] = 1
    
    for i in graph[x]:
        if visit[i]:
            continue
        dep[i] = dep[x]+1
        parent[i][0] = x
        q.append(i)


for i in range(1,log):
    for x in range(1,n+1):
        parent[x][i] = parent[parent[x][i-1]][i-1]


m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    dx = dep[x]
    dy = dep[y]
    if dx>dy:
        diff = dx-dy
        for i in range(log-1,-1,-1):
            if diff>=(1<<i):
                diff -= (1<<i)
                x = parent[x][i]
    elif dy>dx:
        diff = dy-dx
        for i in range(log-1,-1,-1):
            if diff>=(1<<i):
                diff -= (1<<i)
                y = parent[y][i]
    
    
    if x==y:
        print(x)
    else:
        for i in range(log-1,-1,-1):
            nx = parent[x][i]
            ny = parent[y][i]
            if nx==ny:
                continue
            x = nx
            y = ny
        
        print(parent[x][0])