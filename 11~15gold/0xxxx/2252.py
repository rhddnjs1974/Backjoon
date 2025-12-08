import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

V,E = map(int,input().split())
indegree= [0]*(V+1)
graph = [[] for i in range(V+1)]

for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())