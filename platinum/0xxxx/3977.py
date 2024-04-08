import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(cur):
    global h
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
            scc_index[node] = h
            if cur == node:
                break
        h+=1
    return parent

T = int(input())
for x in range(T):
    h = 0
    if x!=0:
        a = input()
    v, e = map(int, input().split())

    graph = [[] for i in range(v)]

    scc_index = [-1]*(v)

    arr = []

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        arr.append((a,b))

    visit = [-1] * (v)
    stack = []
    on_stack = [False] * (v)
    id = 0

    for i in range(v):
        if visit[i] == -1:
            dfs(i)

    m = max(scc_index)

    indegree_scc = [0]*(m+1)

    for i,j in arr:
        if scc_index[i]!=scc_index[j]:
            indegree_scc[scc_index[j]]+=1

    ans = 0

    for i in range(m+1):
        if indegree_scc[i]==0:
            ans+=1
            ans2 = i

    if ans>1:
        print("Confused")
    else:
        if ans==1:
            for i in range(v):
                if scc_index[i]==ans2:
                    print(i)
        else:
            for i in range(v):
                print(i)
    print()



