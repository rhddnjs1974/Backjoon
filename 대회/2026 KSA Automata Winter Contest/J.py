import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

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
    
S = int(input())

if S == 1: #앨리스
    T = int(input())
    out = []

    for _ in range(T):
        N = int(input())
        w = [0] + list(map(int, input().split()))
        g = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        arr = list(range(1, N+1))
        arr.sort(key=lambda x: w[x])

        parent_uf = [0] * (N+1)

        active = [0] * (N+1)
        root = [0] * (N+1)


        for v in arr:
            active[v] = 1
            parent_uf[v] = v
            root[v] = v

            t = []
            s = set()

            for u in g[v]:
                if not active[u]:
                    continue
                r = find(u)
                if r in s:
                    continue
                s.add(r)
                t.append(r)

            for r in t:
                print(v, root[r])

            for r in t:
                union(v, r)

            root[find(v)] = v

        sys.stdout.flush()

else: #밥
    T = int(input())

    for _ in range(T):
        N = int(input())
        
        g = [[] for _ in range(N + 1)]
        
        for _ in range(N - 1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)

        cand = 1
        for i in range(2, N + 1):
            print("?",cand,i)
            sys.stdout.flush()
            
            ans = int(input())
            cand = ans

        root = cand

        lca_init(N, g, root)

        print("!")
        for i in range(1,N+1):
            for j in range(1,N+1):
                print(str(lca(i,j)),end=" ")
            print()
        sys.stdout.flush()