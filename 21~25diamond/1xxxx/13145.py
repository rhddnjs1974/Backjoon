import sys
import math
import heapq
input = sys.stdin.readline

def dijkstra_primal(n, g):
    inf = 10**30
    dist = [inf]*(n+1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        cd, u = heapq.heappop(pq)
        if cd != dist[u]:
            continue
        if u == n:
            return cd
        for v, w in g[u]:
            nd = cd+w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist[n]

def dijkstra_dual(fcnt, dg, s, t):
    inf = 10**30
    dist0 = [inf]*fcnt
    dist1 = [inf]*fcnt
    dist0[s] = 0
    pq = [(0, s, 0)]
    while pq:
        cd, u, used = heapq.heappop(pq)
        if used == 0:
            if cd != dist0[u]:
                continue
        else:
            if cd != dist1[u]:
                continue
        for v, w in dg[u]:
            nd = cd+w
            if used == 0:
                if nd < dist0[v]:
                    dist0[v] = nd
                    heapq.heappush(pq, (nd, v, 0))
                if cd < dist1[v]:
                    dist1[v] = cd
                    heapq.heappush(pq, (cd, v, 1))
            else:
                if nd < dist1[v]:
                    dist1[v] = nd
                    heapq.heappush(pq, (nd, v, 1))
    return dist1[t]

n = int(input())
x = [0]*(n+3)
y = [0]*(n+3)
mi_y = 10**18
for i in range(1, n+1):
    x[i], y[i] = map(int, input().split())
    mi_y = min(mi_y, y[i])

p = n+1
q = n+2
x[p] = x[1]-1
y[p] = mi_y-1
x[q] = x[n]+1
y[q] = mi_y-1

m = int(input())

u = [0]*(m+3)
v = [0]*(m+3)
w = [0]*(m+3)

g = [[] for _ in range(n+1)]
tot = 0

for i in range(m):
    u[i], v[i], w[i] = map(int, input().split())
    g[u[i]].append((v[i], w[i]))
    g[v[i]].append((u[i], w[i]))
    tot += w[i]

ans1 = dijkstra_primal(n, g)

u[m] = 1
v[m] = p
w[m] = 0

u[m+1] = p
v[m+1] = q
w[m+1] = 0

u[m+2] = q
v[m+2] = n
w[m+2] = 0

e = m+3
adj = [[] for _ in range(n+3)]
ang = [0.0]*(2*e)

for i in range(e):
    h0 = i * 2
    h1 = h0 + 1
    adj[u[i]].append(h0)
    adj[v[i]].append(h1)
    ang[h0] = math.atan2(y[v[i]]-y[u[i]], x[v[i]]-x[u[i]])
    ang[h1] = math.atan2(y[u[i]]-y[v[i]], x[u[i]]-x[v[i]])

for i in range(1, n+3):
    adj[i].sort(key=lambda z: ang[z])

pos = [0]*(2*e)
for i in range(1, n+3):
    for j in range(len(adj[i])):
        pos[adj[i][j]] = j

nxt = [0]*(2*e)
for i in range(e):
    h0 = i * 2
    h1 = h0 + 1

    to0 = v[i]
    lst = adj[to0]
    nxt[h0] = lst[(pos[h1]-1) % len(lst)]

    to1 = u[i]
    lst = adj[to1]
    nxt[h1] = lst[(pos[h0]-1) % len(lst)]

face = [-1]*(2*e)
fcnt = 0

for i in range(2*e):
    if face[i] != -1:
        continue
    cur = i
    while face[cur] == -1:
        face[cur] = fcnt
        cur = nxt[cur]
    fcnt += 1

mid = m+1
s = face[mid * 2]
t = face[mid * 2 + 1]

dg = [[] for _ in range(fcnt)]
for i in range(m):
    a = face[i * 2]
    b = face[i * 2 + 1]
    dg[a].append((b, w[i]))
    dg[b].append((a, w[i]))

best_cut_minus_max = dijkstra_dual(fcnt, dg, s, t)
ans2 = tot-best_cut_minus_max

print(ans1, ans2)