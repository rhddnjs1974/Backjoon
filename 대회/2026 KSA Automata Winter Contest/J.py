import sys
input = sys.stdin.readline
sys.setrecursionlimit(3*(10**5))
from collections import deque

# ---- LCA Library (Sparse Table) ----
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

def up_k(v, k):
    # v를 k칸 위 조상으로 올림
    for j in range(LOG):
        if k & (1 << j):
            v = parent[v][j]
    return v

################################################

def find(x):
    if parent_uf[x] != x:
        parent_uf[x] = find(parent_uf[x])
    return parent_uf[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent_uf[b] = a
    else:
        parent_uf[a] = b
    
def alice_build_merge_tree(n, w, edges):
    global parent_uf
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    order = list(range(1, n + 1))
    order.sort(key=lambda x: w[x], reverse=True)

    active = [False] * (n + 1)

    parent_uf = list(range(n + 1))

    cart_root = [0] * (n + 1)
    parH = [0] * (n + 1)

    for v in order:
        active[v] = True
        cart_root[v] = v

        re = []
        for to in g[v]:
            if active[to]:
                re.append(find(to))

        uniq = []
        seen = set()
        for r in re:
            if r not in seen:
                seen.add(r)
                uniq.append(r)

        for c in uniq:
            r = cart_root[c]
            parH[r] = v

        base = v
        for c in uniq:
            union(base, c)
            base = find(base)
        cart_root[find(base)] = v

    out = []
    for x in range(1, n + 1):
        if parH[x] != 0:
            out.append((parH[x], x))
    return out

# 밥 용

def bfs_far(n, g, start):
    dist = [-1] * (n + 1)
    par = [0] * (n + 1)
    q = deque([start])
    dist[start] = 0
    last = start
    while q:
        v = q.popleft()
        last = v
        for to in g[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            par[to] = v
            q.append(to)
    return last, par, dist

def diameter_path(n, g):
    u, trash, trash2 = bfs_far(n, g, 1)
    v, par, trash = bfs_far(n, g, u)
    path = []
    cur = v
    while cur != 0:
        path.append(cur)
        if cur == u:
            break
        cur = par[cur]
    path.reverse()
    return u, v, path

def comp_sizes_around(n, g, r):
    se = [False] * (n + 1)
    se[r] = True
    co = []
    for nb in g[r]:
        if se[nb]:
            continue
        q = deque([nb])
        se[nb] = True
        nodes = [nb]
        while q:
            v = q.popleft()
            for to in g[v]:
                if to == r or se[to]:
                    continue
                se[to] = True
                q.append(to)
                nodes.append(to)
        co.append((len(nodes), nb, nodes))
    return co

def farthest_in_subset(n, g, start, banned, allow):
    dist = [-1] * (n + 1)
    q = deque()
    if start == banned or start not in allow:
        start = next(iter(allow))
    dist[start] = 0
    q.append(start)
    last = start
    while q:
        v = q.popleft()
        last = v
        for to in g[v]:
            if to == banned or dist[to] != -1:
                continue

            dist[to] = dist[v] + 1
            q.append(to)
    return last


def bob_find_root(n, g, ask):
    u, v, path = diameter_path(n, g)
    L = len(path) - 1

    used = 0
    if L % 2 == 0:
        r0 = path[L // 2]
    else:
        c1 = path[L // 2]
        c2 = path[L // 2 + 1]
        ans = ask(c1, c2)
        used = 1
        r0 = ans

    comps = comp_sizes_around(n, g, r0)
    mx = 0
    big_nodes = None
    big_nb = 0
    for sz, nb, nodes in comps:
        if sz > mx:
            mx = sz
            big_nodes = nodes
            big_nb = nb

    if used < 2 and mx * 2 > n and big_nodes is not None:
        big_set = set(big_nodes)
        a = farthest_in_subset(n, g, big_nb, r0, big_set)

        outside = set(range(1, n + 1))
        outside.discard(r0)
        for x in big_nodes:
            outside.discard(x)

        if outside:
            b0 = next(iter(outside))
            b = farthest_in_subset(n, g, b0, r0, outside)
        else:
            b = big_nb

        ans2 = ask(a, b)
        r0 = ans2

    return r0


S = int(input().strip())
T = int(input().strip())

if S == 1:
    for _ in range(T):
        n = int(input().strip())
        w_list = list(map(int, input().split()))
        w = [0] * (n + 1)
        for i in range(1, n + 1):
            w[i] = w_list[i - 1]

        edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
        bridges = alice_build_merge_tree(n, w, edges)
        for a, b in bridges:
            print(a,b)
    sys.stdout.flush()
else:
    for _ in range(T):
        n = int(input().strip())
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        def ask(i, j):
            print("?",i,j)
            sys.stdout.flush()
            x = int(input().strip())
            if x == -1:
                sys.exit(0)
            return x

        root = bob_find_root(n, g, ask)

        lca_init(n, g, root)

        print("!")
        sys.stdout.flush()
        for i in range(1, n + 1):
            row = []
            for j in range(1, n + 1):
                row.append(str(lca(i, j)))
            print(*row)
        sys.stdout.flush()