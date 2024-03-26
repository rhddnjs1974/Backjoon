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

V,m,E = map(int,input().split())
graph = [[] for i in range(V+1)]

item_array = list(map(int,input().split()))

for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u, w))


ma = 0
for i in range(1,V+1):
    distance = [INF] * (V + 1)
    dijkstra(i)
    item =0
    for j in range(1,V+1):
        if distance[j]<=m:
            item+=item_array[j-1]
    ma = max(ma,item)

print(ma)