import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

def dfs(cur):
    global id, h
    id += 1
    visit[cur] = id
    stack.append(cur)
    on_stack[cur] = True

    parent = visit[cur]
    for next in graph[cur]:
        if visit[next] == -1:
            parent = min(parent, dfs(next))
        elif on_stack[next]:
            parent = min(parent, visit[next])

    if parent == visit[cur]:
        scc = []
        s = 0
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc.append(node)
            scc_index[node] = h
            s+=atm[node]
            if cur == node:
                break
        h+=1
        atm_scc.append(s)
    return parent


def topology_sort():
    global s
    result = []
    q = deque()

    q.append(scc_index[s])
    dp[scc_index[s]] = atm_scc[scc_index[s]]



    while q:
        now = q.popleft()
        visit2[now] = 1
        result.append(now)
        for i in graph2[now]:
            indegree_scc[i]-=1
            dp[i] = max(dp[i], dp[now] + atm_scc[i])
            if visit2[i]==0 and indegree_scc[i]<=0:
                q.append(i)


    return result



h = 0
v, e = map(int, input().split())

graph = [[] for i in range(v+1)]

scc_index = [-1]*(v+1)

arr = []

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    arr.append((a,b))

atm = [0]
atm_scc = []
for i in range(v):
    atm.append(int(input()))

s,p = map(int,input().split())
P = list(map(int,input().split()))

visit = [-1] * (v+1)
stack = []
on_stack = [False] * (v+1)
id = 0

for i in range(1,v+1):
    if visit[i] == -1:
        dfs(i)

m = max(scc_index)

indegree_scc = [0]*(m+1)

graph2= [[] for i in range(m+1)]
for i,j in arr:
    a = scc_index[i]
    b = scc_index[j]
    if a!=b:
        if b not in graph2[a]:
            graph2[a].append(b)
            indegree_scc[b] += 1

dp = [0]*(m+1)

visit2 = [0]*(m+1)
s = 1
x = topology_sort()

ans = 0
for i in P:
    a = scc_index[i]
    ans = max(ans,dp[a])
print(ans)