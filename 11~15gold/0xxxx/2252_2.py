import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q = []
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while(q):
    x = q.pop()
    print(x,end=" ")
    for i in graph[x]:
        indegree[i] -=1
        if indegree[i]==0:
            q.append(i)

