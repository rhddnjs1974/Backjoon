import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

def dfs(cur):
    global id,scc_num
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
        scc_num +=1
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc_id[node] = scc_num
            scc.append(node)
            if cur == node:
                break
        ans.append(scc)
    return parent

def dfs2(now):
    visit2[now] = 1
    if now<=n:
        t = now+n
    else:
        t = now-n
    visit2[t] = 0
    for next in graph[now]:
        print(now,next)
        if visit2[next]==-1:
            dfs2(next)

arr = []
n,m = map(int,input().split())
scc_id = [0]*(2*n+1)
scc_num = 0

graph = [[] for i in range(2*n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr.append((a,b))
    if a>0 and b>0:
        graph[a+n].append(b)
    if a>0 and b<0:
        graph[a+n].append(-b+n)
    if a<0 and b>0:
        graph[-a].append(b)
    if a<0 and b<0:
        graph[-a].append(-b+n)

    b,a = a,b
    if a>0 and b>0:
        graph[a+n].append(b)
    if a>0 and b<0:
        graph[a+n].append(-b+n)
    if a<0 and b>0:
        graph[-a].append(b)
    if a<0 and b<0:
        graph[-a].append(-b+n)

visit = [-1] * (2*n+1)
stack = []
on_stack = [False] * (2*n+1)
id = 0
ans = []

for i in range(1,2*n+1):
    if visit[i] == -1:
        dfs(i)

flag = 1
for i in range(1,n+1):
    if scc_id[i]==scc_id[i+n]:
        flag=0
        break


print(flag)

if flag==1:

    visit2 = [-1]*(n*2+1)
    print(ans)
    for i in ans[::-1]:
        for j in i:
            print(j)
            if visit2[j]==-1:
                visit2[j] = 0
                if j<=n:
                    dfs2(j+n)
                else:
                    dfs2(j-n)

    print(visit2)

