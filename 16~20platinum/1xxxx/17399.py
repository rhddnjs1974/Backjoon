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

def up(x, k):
    j = 0
    while k:
        if k & 1:
            x = parent[x][j]
        k >>= 1
        j += 1
    return x

def kth_on_path(u, v, k):
    w = lca(u, v)
    du = dep[u] - dep[w]
    dv = dep[v] - dep[w]
    d = du + dv

    if k <= du:
        return up(u, k)

    return up(v, d - k)

def circumcenter_two(u, v):
    d = dist(u, v)
    if d & 1:
        return -1
    return kth_on_path(u, v, d // 2)


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

lca_init(N, graph, 1)

Q = int(input())
for _ in range(Q):
    A, B, C = map(int, input().split())

    if A == B == C:
        print(A)
        continue
    if A == B:
        print(circumcenter_two(A, C))
        continue
    if A == C:
        print(circumcenter_two(A, B))
        continue
    if B == C:
        print(circumcenter_two(B, A))
        continue

    x = lca(A, B)
    y = lca(B, C)
    z = lca(C, A)

    m = x
    if dep[y] > dep[m]:
        m = y
    if dep[z] > dep[m]:
        m = z

    da = dist(m, A)
    db = dist(m, B)
    dc = dist(m, C)

    ans = -1

    if db == dc and da >= db:
        diff = da - db
        if diff % 2 == 0:
            t = diff // 2
            ans = kth_on_path(A, m, da - t)

    if ans == -1 and da == dc and db >= da:
        diff = db - da
        if diff % 2 == 0:
            t = diff // 2
            ans = kth_on_path(B, m, db - t)

    if ans == -1 and da == db and dc >= da:
        diff = dc - da
        if diff % 2 == 0:
            t = diff // 2
            ans = kth_on_path(C, m, dc - t)

    print(ans)