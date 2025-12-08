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

V = int(input())
D = [0]*(V+1)
indegree= [0]*(V+1)
graph = [[] for i in range(V+1)]
dp = [0]*(V+1)

for i in range(1,V+1):
    a,*b = map(int,input().split())
    D[i] = a
    for j in b:
        if j==-1:
            break
        graph[j].append(i)
        indegree[i] += 1

topology_sort()
for i in range(1,V+1):
    print(dp[i]+D[i])
