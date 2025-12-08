import sys
input = sys.stdin.readline
from collections import deque
import heapq

def topology_sort():
    result = []
    q = []

    for i in range(1,V+1):
        if indegree[i]==0:
            heapq.heappush(q,i)

    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(q, i)

    return result

V,E = map(int,input().split())
indegree= [0]*(V+1)
graph = [[] for i in range(V+1)]

for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1,V+1):
    graph[i].sort()

print(*topology_sort())