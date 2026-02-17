import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(3*(10**5))

def dfs(cur):
    global dfs_id
    dfs_id += 1
    visit[cur] = dfs_id
    stack.append(cur)
    on_stack[cur] = True

    parent = visit[cur]
    for nxt in graph[cur]:
        if visit[nxt] == -1:
            v = dfs(nxt)
            if v < parent:
                parent = v
        elif on_stack[nxt]:
            v = visit[nxt]
            if v < parent:
                parent = v

    if parent == visit[cur]:
        comp = []
        while True:
            node = stack.pop()
            on_stack[node] = False
            comp.append(node)
            if node == cur:
                break
        sccs.append(comp)

    return parent

n, m = map(int, input().split())
p_str = input().split()

graph = [[] for _ in range(n + 1)]
edges_a = [0] * m
edges_b = [0] * m
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    edges_a[i] = a
    edges_b[i] = b

visit = [-1] * (n + 1)
stack = []
on_stack = [False] * (n + 1)
dfs_id = 0
sccs = []

for i in range(1, n + 1):
    if visit[i] == -1:
        dfs(i)

k = len(sccs)
comp_id = [-1] * (n + 1)
for cid in range(k):
    for v in sccs[cid]:
        comp_id[v] = cid

logW = [0.0] * k
for v in range(1, n + 1):
    cid = comp_id[v]
    q = 1.0 - float(p_str[v - 1])
    if q <= 0.0:
        logW[cid] = float('-inf')
    else:
        if logW[cid] != float('-inf'):
            logW[cid] += math.log(q)

out = [False] * k
for i in range(m):
    ca = comp_id[edges_a[i]]
    cb = comp_id[edges_b[i]]
    if ca != cb:
        out[ca] = True

best = float('-inf')
for cid in range(k):
    if not out[cid]:
        if logW[cid] > best:
            best = logW[cid]

if best == float('-inf'):
    ans = 0.0
else:
    ans = math.exp(best)

print(ans)
