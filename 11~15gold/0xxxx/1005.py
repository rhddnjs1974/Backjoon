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
            dp[i] = max(dp[i], dp[now] + D[now])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)


    return result

T = int(input())
for i in range(T):
    V,E = map(int,input().split())
    D = [0]+list(map(int,input().split()))
    indegree= [0]*(V+1)
    graph = [[] for i in range(V+1)]
    dp = [0]*(V+1)

    for i in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1

    W = int(input())

    topology_sort()
    print(dp[W]+D[W])