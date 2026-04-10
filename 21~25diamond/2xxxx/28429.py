# 라이브러리: 최소공통조상.py
import sys
input = sys.stdin.readline

def lca(x, y):
    if dep[x] > dep[y]:
        x, y = y, x
    d = dep[y]-dep[x]
    for j in range(LOG):
        if (d >> j) & 1:
            y = pa[j][y]
    if x == y:
        return x
    for j in range(LOG-1, -1, -1):
        if pa[j][x] != pa[j][y]:
            x = pa[j][x]
            y = pa[j][y]
    return pa[0][x]

def up_k(v, k):
    for j in range(LOG):
        if (k >> j) & 1:
            v = pa[j][v]
    return v

def is_anc(u, v):
    return tin[u] <= tin[v] and tout[v] <= tout[u]

def path_sum(u, v):
    l = lca(u, v)
    return dist[u]+dist[v]-2 * dist[l]+A[l]

def get_ext(endpoint, toward):
    if is_anc(endpoint, toward):
        cb = up_k(toward, dep[toward]-dep[endpoint]-1)
        if b1c[endpoint] != cb:
            od = b1[endpoint]
        else:
            od = b2[endpoint]
        val = up[endpoint]
        if od > val and od > -INF:
            val = od
        return max(0, val)
    ext = b1[endpoint]
    if ext > 0:
        return ext
    return 0

n, q = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
A = [0] + list(map(int, input().split()))

LOG = max(1, n.bit_length())
pa = [[0] * (n+1) for _ in range(LOG)]
dep = [0] * (n+1)
tin = [0] * (n+1)
tout = [0] * (n+1)
order = []
ch = [[] for _ in range(n+1)]

t = 0
stk = [(1, 0, False)]
while stk:
    v, p, leaving = stk.pop()
    if leaving:
        tout[v] = t
        t += 1
        continue
    pa[0][v] = p
    if p:
        dep[v] = dep[p]+1
    tin[v] = t
    t += 1
    order.append(v)
    stk.append((v, p, True))
    for u in reversed(g[v]):
        if u != p:
            ch[v].append(u)
            stk.append((u, v, False))

for k in range(1, LOG):
    for v in range(1, n+1):
        pa[k][v] = pa[k-1][pa[k-1][v]]

INF = float('inf')
down = [0] * (n+1)
b1 = [-INF] * (n+1)
b1c = [0] * (n+1)
b2 = [-INF] * (n+1)

for v in reversed(order):
    mx = -INF
    mxc = 0
    mx2 = -INF
    for c in ch[v]:
        if down[c] > mx:
            mx2 = mx
            mx = down[c]
            mxc = c
        elif down[c] > mx2:
            mx2 = down[c]
    b1[v] = mx
    b1c[v] = mxc
    b2[v] = mx2
    down[v] = A[v]
    if mx > 0:
        down[v] += mx

up = [0] * (n+1)
for v in order:
    for c in ch[v]:
        if b1c[v] != c:
            other = b1[v]
        else:
            other = b2[v]
        val = up[v]
        if other > val and other > -INF:
            val = other
        if val > 0:
            up[c] = A[v]+val
        else:
            up[c] = A[v]

dist = [0] * (n+1)
for v in order:
    if pa[0][v]:
        dist[v] = dist[pa[0][v]]+A[v]
    else:
        dist[v] = A[v]

for _ in range(q):
    line = list(map(int, input().split()))
    k = line[0]
    S = line[1:k+1]

    if k == 1:
        v = S[0]
        cands = []
        if pa[0][v]:
            cands.append(up[v])
        if b1[v] > -INF:
            cands.append(b1[v])
        if b2[v] > -INF:
            cands.append(b2[v])
        cands.sort(reverse=True)
        e1 = 0
        e2 = 0
        if cands and cands[0] > 0:
            e1 = cands[0]
        if len(cands) >= 2 and cands[1] > 0:
            e2 = cands[1]
        print(A[v]+e1+e2)
        continue

    S.sort(key=lambda x: tin[x])

    nodes = list(S)
    for i in range(len(S)-1):
        nodes.append(lca(S[i], S[i+1]))
    nodes = list(set(nodes))
    nodes.sort(key=lambda x: tin[x])

    vdeg = {}
    for nd in nodes:
        vdeg[nd] = 0

    stk2 = [nodes[0]]
    for i in range(1, len(nodes)):
        v = nodes[i]
        l = lca(v, stk2[-1])
        if l != stk2[-1]:
            while len(stk2) > 1 and dep[stk2[-2]] >= dep[l]:
                vdeg[stk2[-2]] += 1
                vdeg[stk2[-1]] += 1
                stk2.pop()
            if stk2[-1] != l:
                vdeg[l] += 1
                vdeg[stk2[-1]] += 1
                stk2[-1] = l
        stk2.append(v)
    while len(stk2) > 1:
        vdeg[stk2[-2]] += 1
        vdeg[stk2[-1]] += 1
        stk2.pop()

    ok2 = True
    eps = []
    for nd in vdeg:
        if vdeg[nd] > 2:
            ok2 = False
            break
        if vdeg[nd] <= 1:
            eps.append(nd)

    if not ok2:
        print("No")
        continue

    a, b = eps[0], eps[-1]
    mand = path_sum(a, b)
    print(mand+get_ext(a, b)+get_ext(b, a))