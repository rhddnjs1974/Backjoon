import sys
input = sys.stdin.readline
INF = int(1e9)

CYCLE= []
dont = []
def Bellman_ford(start):
    dist[start] = 0
    for i in range(V):
        for j in range(E): ## a->b
            node_a = edge[j][0]
            node_b = edge[j][1]
            if node_b in dont:
                continue
            cost = edge[j][2]

            if dist[node_a]!=INF and dist[node_b] > dist[node_a] + cost:
                dist[node_b] = dist[node_a] + cost
                pre[node_b] = node_a

                if i>=V-1:
                    CYCLE.append(node_b)
    if CYCLE:
        return True
    return False

def cantreach(arr,v):
    visit = [0]*(V+1)
    while(arr):
        x = arr.pop()
        visit[x]=1
        for i in graph[x]:
            if visit[i]==0:
                arr.append(i)
    if visit[v]==0:
        return True
    return False

V,E = map(int,input().split())

edge = []
dist = [INF]*(V+1)
pre = [0]*(V+1)

graph = [[] for i in range(V+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(b)
    edge.append((a,b,-c))

minus_cycle = Bellman_ford(1)

if minus_cycle or dist[V]==INF:
    if cantreach(CYCLE,V):
        dont = CYCLE[::]
        dist = [INF]*(V+1)
        pre = [0]*(V+1)
        Bellman_ford(1)
        x=[V]
        now = V
        while(now!=1):
            now = pre[now]
            x.append(now)
        x = x[::-1]
        print(*x) 
        
    else:
        print(-1)
else:
    x=[V]
    now = V
    while(now!=1):
        now = pre[now]
        x.append(now)
    x = x[::-1]
    print(*x)