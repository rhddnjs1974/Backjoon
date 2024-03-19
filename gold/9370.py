import heapq
import sys
input = sys.stdin.readline
from collections import deque
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
                route[a] = [now]
                heapq.heappush(heap,(cost,a))
            elif cost==distance[a]:
                route[a].append(now)

def bfs(v):
    visit[v] = 1
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        for j in route[i]:
            if visit[j]==0:
                visit[j] = 1
                q.append(j)

T = int(input())
for i in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u, w))

    route = [[0] for i in range(n+1)]

    hubo = []
    for i in range(t):
        hubo.append(int(input()))

    dijkstra(s)



    ans=[]
    if h in route[g]:
        find = g
    else:
        find = h

    for i in hubo:
        visit = [0]*(n+1)
        bfs(i)
        if visit[find]==1:
            ans.append(i)

    ans.sort()
    print(*ans)
