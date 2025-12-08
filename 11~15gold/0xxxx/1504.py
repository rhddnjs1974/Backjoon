import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
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
            cost = dist + b
            if cost < distance[a]:
                distance[a] = cost
                heapq.heappush(heap,(cost,a))

V,E = map(int,input().split())
graph = [[] for i in range(V+1)]


for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1,v2 = map(int,input().split())

distance = [INF] * (V+1)
dijkstra(1)
a = distance[v1]
b = distance[v2]

distance = [INF] * (V+1)
dijkstra(v1)
a2 = distance[v2]
b3 = distance[V]

distance = [INF] * (V+1)
dijkstra(v2)
a3 = distance[V]
b2 = distance[v1]

ans = min((a+a2+a3),(b+b2+b3))

if ans>=INF:
    print(-1)
else:
    print(ans)
