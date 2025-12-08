import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    visit[v] = 1
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        for j in graph[i]:
            if visit[j]==0:
                visit[j] = visit[i]+1
                q.append(j)

N = int(input())
x,y = map(int,input().split())
M = int(input())
#N:정점개수 / M:간선개수 / V:탐색시작번호

graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visit = [0]*(N+1)
bfs(x)

print(visit[y]-1)