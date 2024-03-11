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
K = int(input())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dijkstra(K)


for i in range(1,V+1):

    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])