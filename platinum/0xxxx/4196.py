import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur):
    global id
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
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc.append(node)
            scc_index[node] = len(ans)
            if cur == node:
                break
        ans.append(scc)
    return parent

T = int(input())
for i in range(T):
    v, e = map(int, input().split())

    graph = [[] for i in range(v+1)]

    scc_index = [-1]*(v+1)

    arr = []

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        arr.append((a,b))

    visit = [-1] * (v+1)
    stack = []
    on_stack = [False] * (v+1)
    id = 0
    ans = []

    for i in range(1,v+1):
        if visit[i] == -1:
            dfs(i)


    m = max(scc_index)
    indegree_scc = [0]*(m+1)

    for i,j in arr:
        if scc_index[i]!=scc_index[j]:
            indegree_scc[scc_index[j]]+=1

    ans = 0
    for i in indegree_scc:
        if i==0:
            ans+=1
    print(ans)

