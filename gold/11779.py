import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################
def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    distance[start] = 0
    route[start] = [start]
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for a,b in graph[now]:
            cost = dist + b
            if cost < distance[a]:
                route[a] = []
                for i in route[now]:
                    route[a].append(i)
                route[a].append(a)
                distance[a] = cost
                heapq.heappush(heap,(cost,a))

V = int(input())
E = int(input())

graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

start,end = map(int,input().split())

route = [[] for i in range(V+1)]

dijkstra(start)

print(distance[end])
print(len(route[end]))
for i in route[end]:
    print(i,end=" ")