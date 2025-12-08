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

n,m,k = map(int,input().split())
graph = []
for i in range(n*2):
    graph.append([])

for i in range(n):
    a,*arr = map(int,input().split())
    graph[i] = arr
    graph[i+n] = arr

connect = [-1]*(m+1)

t = 0
for i in range(n*2):
    visit = [0]*(n*2)
    if match(i) and i>=n:
        t+=1
        if t==k:
            break

ans = 0
for i in range(1,m+1):
    if connect[i]!=-1:
        ans+=1

print(ans)