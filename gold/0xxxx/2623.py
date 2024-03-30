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
    t,*arr = list(map(int,input().split()))

    for j in range(t):
        for k in range(j+1,t):
            graph[arr[j]].append(arr[k])
            indegree[arr[k]] += 1


ans = topology_sort()
if len(ans)==V:
    for i in ans:
        print(i)
else:
    print(0)