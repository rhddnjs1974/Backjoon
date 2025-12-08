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

V,E,K,X = map(int,input().split())

graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    u,v = map(int,input().split())
    graph[u].append((v,1))

dijkstra(X)

ans = []
for i in range(1,V+1):
    if distance[i] == K:
        ans.append(i)

if len(ans)==0:
    print(-1)
else:
    for i in ans:
        print(i)