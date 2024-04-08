import sys
input = sys.stdin.readline

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
            if cur == node:
                break
        ans.append(scc)
    return parent


v, e = map(int, input().split())

graph = [[] for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

visit = [-1] * (v+1)
stack = []
on_stack = [False] * (v+1)
id = 0
ans = []

for i in range(1,v+1):
    if visit[i] == -1:
        dfs(i)

print(len(ans))
ans.sort()
for i in ans:
    i.sort()
    i.append(-1)
    print(*i)