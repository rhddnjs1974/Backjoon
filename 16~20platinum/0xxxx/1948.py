import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
rgraph = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    rgraph[v].append((u, w))
    indeg[v] += 1
start, end = map(int, input().split())

dist = [0] * (n+1)
q = deque()
q.append(start)
while q:
    u = q.popleft()
    for v, w in graph[u]:
        if dist[u]+w > dist[v]:
            dist[v] = dist[u]+w
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

ans = 0
visited = [False] * (n+1)
q.append(end)
visited[end] = True
while q:
    v = q.popleft()
    for u, w in rgraph[v]:
        if dist[u]+w == dist[v]:
            ans += 1
            if not visited[u]:
                visited[u] = True
                q.append(u)

print(dist[end])
print(ans)
