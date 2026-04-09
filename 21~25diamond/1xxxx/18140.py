import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
deg = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    deg[a] += 1
    deg[b] += 1

par = [0] * (n+1)
order = [1]

for u in order:
    for v in graph[u]:
        if v == par[u]:
            continue
        par[v] = u
        order.append(v)

INF = 10**18
f = [[[INF] * 2 for _ in range(3)] for __ in range(n+1)]

for u in order[::-1]:
    f[u][1][0] = 1
    f[u][2][0] = 0

    if deg[u] == 1 and par[u] != 0:
        continue

    f[u][0][0] = 0
    f[u][0][1] = 0
    f[u][2][0] = 0
    f[u][2][1] = 0

    g0 = 0
    g1 = INF

    t00 = 0
    t01 = INF
    t10 = INF
    t11 = INF

    for v in graph[u]:
        if v == par[u]:
            continue

        x = min(f[v][1][0], f[v][0][1], f[v][0][0])

        g1 = min(g1+x, g0+min(f[v][1][0], f[v][0][0]))
        g0 = g0+x

        t11 = min(t11+x, t01+min(f[v][1][0], f[v][0][0]), t10+min(f[v][2][1], f[v][2][0]))
        t01 = min(t01+x, t00+min(f[v][2][1], f[v][2][0]))
        t10 = min(t10+x, t00+min(f[v][1][0], f[v][0][0]))    
        t00 = t00+x

        f[u][1][0] += min(f[v][1][0], f[v][0][0], f[v][0][1], f[v][2][0], f[v][2][1])
        f[u][2][1] = min(f[u][2][0]+min(f[v][2][1], f[v][2][0]), f[u][2][1]+f[v][0][1])
        f[u][2][0] += f[v][0][1]

    f[u][0][0] = g1
    f[u][0][1] = t11

print(min(f[1][1][0], f[1][0][0], f[1][0][1]))