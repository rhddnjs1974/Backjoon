import sys
input = sys.stdin.readline
########################################

def dfs(v):
    visit[v] = 1
    result.append(v)
    for i in graph[v]:
        if visit[i]==0:
            dfs(i)


N,M,V = map(int,input().split())
#N:정점개수 / M:간선개수 / V:탐색시작번호

graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visit = [0]*(N+1)
result = []
dfs(V)
print(*result)
