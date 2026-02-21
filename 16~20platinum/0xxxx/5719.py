import heapq
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e18)
############################################
def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for a,b in graph[now]:
            
            if (now,a) in dontedge:
                continue
            
            cost = dist + b
            if cost < distance[a]:
                distance[a] = cost
                heapq.heappush(heap,(cost,a))


while(True):
    V,E = map(int,input().split())
    if V==0 and E==0:
        break
    S,D = map(int,input().split())

    graph = [[] for i in range(V)]
    graphreverse = [[] for i in range(V)]
    distance = [INF] * (V)

    for i in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graphreverse[v].append((u,w))

    dontedge = set()
    dijkstra(S)

    if distance[D]==INF:
        print(-1)
        continue
    
    dontpoint = set()
    q = deque([D])
    dontpoint.add(D)
    
    visit = [0]*V
    visit[D]=1
    while q:
        x = q.popleft()
        
        for a,b in graphreverse[x]:
            if x in dontpoint and distance[a] + b == distance[x]:
                dontpoint.add(a)
                dontedge.add((a,x))
                if visit[a]==0:
                    visit[a]=1
                    q.append(a)
    
    distance = [INF] * (V)

    dijkstra(S)
    
    if distance[D]==INF:
        print(-1)
    else:
        print(distance[D])