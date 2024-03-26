from collections import deque

def bfs(r):
    global num
    num+=1
    order[r] = num
    visit[r] = True
    graph[r].sort()
    q.append(r)

    while(q):
        i = q.popleft()
        graph[i].sort()
        for j in graph[i]:
            if visit[j]==False:
                visit[j] = True
                num+=1
                order[j] = num
                q.append(j)


n,m,r = map(int,input().split())

order = [0]*(n+1)
num = 0

visit = [False]*(n+1)
graph = [[] for i in range(n+1)]

q = deque()

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(r)

for i in range(1,n+1):
    print(order[i])