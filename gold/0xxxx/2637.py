import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    global s
    result = []
    q = deque()

    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)
            dp[i][i] = 1
            s.add(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i,j in graph[now]:
            for k in range(1,V+1):
                dp[i][k] += dp[now][k] * j
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

s = set()
V = int(input())
E = int(input())
dp = [[0]*(V+1) for i in range(V+1)]
indegree= [0]*(V+1)
graph = [[] for i in range(V+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    graph[b].append((a,c))
    indegree[a] += 1
topology_sort()

for i in range(1,V+1):
    if i in s:
        print(i,dp[V][i])