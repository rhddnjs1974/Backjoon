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
        for i,j in graph[now]:
            dp[i] = max(dp[i],dp[now]+j)
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

V = int(input())
E = int(input())
indegree= [0]*(V+1)
dp = [0]*(V+1)
graph = [[] for i in range(V+1)]
r_graph = [[] for i in range(V+1)]

for i in range(E):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    r_graph[b].append((a,t))
    indegree[b] += 1

ST,EN = map(int,input().split())

topology_sort()
print(dp[EN])


ans = set()
now = EN
q = deque()
q.append(now)
while(q):
    now = q.popleft()
    for i,j in r_graph[now]:
        if dp[i]+j == dp[now]:
            q.append(i)
            ans.add((i,now))

print(len(ans))