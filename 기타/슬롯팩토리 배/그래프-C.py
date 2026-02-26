import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()

    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i,w,k in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

N, M, S, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    u, v, w, a, b = map(int, input().split())
    k = 1 - (a / (2 * b))
    graph[u].append((v, w, k))
    indegree[v] += 1

topo = topology_sort()

dp = [-1e300] * (N + 1)
dp[S] = 0.0

for u in topo:
    if dp[u] < 0:
        continue
    
    for (v, w, k) in graph[u]:
        cand = k * (dp[u] + w)
        if cand > dp[v]:
            dp[v] = cand

ans = dp[T]
if ans < 0:
    ans = -1

print(ans)