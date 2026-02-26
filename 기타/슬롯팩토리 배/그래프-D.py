import sys
import math
import heapq

input = sys.stdin.readline

N, M, S, T = map(int, input().split())

edges = []
nodes = {S, T}

for _ in range(M):
    u, v, w, a, b = map(int, input().split())
    k = 1.0 - (a / (2.0 * b))
    edges.append((u, v, w, k))
    nodes.add(u)
    nodes.add(v)

nodes = list(nodes)
idx = {}
for i in range(len(nodes)):
    idx[nodes[i]] = i

K = len(nodes)
S = idx[S]
T = idx[T]

fr = [0] * M
to = [0] * M
w = [0.0] * M
k = [0.0] * M

for i in range(M):
    u, v, ww, kk = edges[i]
    fr[i] = idx[u]
    to[i] = idx[v]
    w[i] = float(ww)
    k[i] = float(kk)

adj_by_edge = [[] for _ in range(K)]
for i in range(M):
    adj_by_edge[fr[i]].append(i)

LOGK = [0.0] * M
for i in range(M):
    LOGK[i] = -math.log(k[i])


size = 1 << M
dp = [[-1e300] * K for _ in range(size)]
dp[0][S] = 0.0

best_T = 0.0

for mask in range(size):
    dist = [1e300] * K
    hq = []

    row = dp[mask]
    for v in range(K):
        val = row[v]
        if val > 0.0:
            d0 = -math.log(val)
            if d0 < dist[v]:
                dist[v] = d0
                heapq.heappush(hq, (d0, v))
        elif val == 0.0:
            pass

    while hq:
        d, x = heapq.heappop(hq)
        if d != dist[x]:
            continue

        for ei in adj_by_edge[x]:
            if (mask >> ei) & 1 == 0:
                continue
            y = to[ei]
            nd = d + LOGK[ei]
            if nd < dist[y]:
                dist[y] = nd
                heapq.heappush(hq, (nd, y))

    best = [0.0] * K
    for v in range(K):
        if dist[v] < 1e300 / 2:
            best[v] = math.exp(-dist[v])

    if best[T] > best_T:
        best_T = best[T]

    for ei in range(M):
        if (mask >> ei) & 1:
            continue
        a = fr[ei]
        base = best[a]
        if base <= 0.0 and base != 0.0:
            continue
        cand = k[ei] * (base + w[ei])
        nmask = mask | (1 << ei)
        b = to[ei]
        if cand > dp[nmask][b]:
            dp[nmask][b] = cand

print(best_T)