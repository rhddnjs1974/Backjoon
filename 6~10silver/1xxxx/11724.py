import sys
input = sys.stdin.readline

def bfs(i):
    a = []
    a.append(i)
    while(a):
        x = a.pop()
        visit[x]=1
        for i in graph[x]:
            if visit[i]==0:
                a.append(i)

    

N,M = map(int,input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0]*(N+1)
ans=0

for i in range(1,N+1):
    if visit[i]==0:
        bfs(i)
        ans+=1

print(ans)