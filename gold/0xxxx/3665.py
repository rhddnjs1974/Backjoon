import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    global flag
    result = []
    q = deque()

    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)
    if len(q)>1:
        flag=1
    while q:
        if len(q)>1:
            flag=1
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    return result

T = int(input())
for i in range(T):
    flag = 0
    V = int(input())
    indegree= [0]*(V+1)
    ti = list(map(int,input().split()))
    E = int(input())
    graph = [[] for i in range(V + 1)]
    for i in range(V):
        for j in range(i+1,V):
            a = ti[i]
            b = ti[j]
            graph[a].append(b)
            indegree[b] += 1

    for i in range(E):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[b] += 1
            indegree[a] -= 1

    ans = topology_sort()
    if len(ans)!=V:
        print("IMPOSSIBLE")
    elif flag==1:
        print("?")
    else:
        print(*ans)
