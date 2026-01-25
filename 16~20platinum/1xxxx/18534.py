import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# ---- LCA Library (Sparse Table) ----
# 사용법:
# 1) graph 채우고
# 2) lca_init(n, graph, root=1) 호출
# 3) lca(x,y), dist(x,y) 호출

LOG = 0
parent = []
dep = []
graph = []

def tree(node, p, depth):
    parent[node][0] = p
    dep[node] = depth
    for nxt in graph[node]:
        if nxt != p:
            tree(nxt, node, depth + 1)

def lca_init(n, g, root=1):
    global LOG, parent, dep, graph
    graph = g
    LOG = (n).bit_length()  # 2^LOG > n

    dep = [0] * (n + 1)
    parent = [[0] * LOG for _ in range(n + 1)]

    tree(root, 0, 0)

    for i in range(1, LOG):
        for v in range(1, n + 1):
            parent[v][i] = parent[parent[v][i - 1]][i - 1]

def lca(x, y):
    if dep[x] > dep[y]:
        x, y = y, x

    diff = dep[y] - dep[x]
    for j in range(LOG - 1, -1, -1):
        if diff >= (1 << j):
            y = parent[y][j]
            diff -= (1 << j)

    if x == y:
        return x

    for j in range(LOG - 1, -1, -1):
        if parent[x][j] != parent[y][j]:
            x = parent[x][j]
            y = parent[y][j]

    return parent[x][0]

def dist(x, y):
    w = lca(x, y)
    return dep[x] + dep[y] - 2 * dep[w]


################################################

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

lca_init(n, graph, 1)

for _ in range(q):
    r, p = map(int, input().split())
    d = dist(r, p)
    print(n + d * (d + 1) // 2)