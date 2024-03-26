import sys
sys.setrecursionlimit(10**5)

def dfs(r):
    global num
    num+=1
    order[r] = num
    visit[r] = True
    graph[r].sort()
    graph[r].reverse()
    for i in graph[r]:
        if visit[i]==False:
            dfs(i)


n,m,r = map(int,input().split())

order = [0]*(n+1)
num = 0

visit = [False]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(r)

for i in range(1,n+1):
    print(order[i])