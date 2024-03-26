import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    parent[v] = 0
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        for j in graph[i]:
            if parent[j]==-1:
                parent[j] = i
                q.append(j)

N = int(input())

graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1]*(N+1)

bfs(1)
for i in range(2,N+1):
    print(parent[i])