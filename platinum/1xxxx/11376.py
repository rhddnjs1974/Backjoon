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
    a,*arr = map(int,input().split())
    graph.append(arr)
    graph.append(arr)

connect = [-1]*(m+1)

for i in range(n*2):
    visit = [0]*(n*2)
    match(i)

ans = 0
for i in range(1,m+1):
    if connect[i]!=-1:
        ans+=1

print(ans)