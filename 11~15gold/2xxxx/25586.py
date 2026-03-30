from collections import deque

N,M,K = map(int,input().split())

grpah = [0]
indegree = [0]*(N+1)
for i in range(N):
    x, *a = map(int,input().split())
    grpah.append(a)
    for j in a:
        indegree[j]+=1

topology = []
q = deque()
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i)

while(q):
    x = q.popleft()
    topology.append(x)
    for i in grpah[x]:
        indegree[i] -= 1
        if indegree[i]==0:
            q.append(i)


ans = [[] for i in range(N+1)]
for i in range(len(topology)-1):
    ans[topology[i]].append(topology[i+1])

print(1)
print(0)
for i in range(1,N+1):
    print(len(ans[i]),*ans[i])