import sys
input = sys.stdin.readline

def match(N):
    if visit[N]!=0:
        return 0
    visit[N] = 1

    for x in graph[N]:
        if connect[x] == -1 or match(connect[x])==1:
            connect[x] = N
            return 1

    return 0

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append([])

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)

connect = [-1]*(n)

for i in range(n):
    visit = [0]*(n)
    match(i)

ans = 0
for i in range(n):
    if connect[i]!=-1:
        ans+=1

print(ans)