import sys
input = sys.stdin.readline
INF = 10**18

N, Q = map(int, input().split())

dist = [[INF] * N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        elif row[j] != 0:
            dist[i][j] = row[j]

groups = [[] for _ in range(N + 1)]
queries = []

for idx in range(Q):
    C, s, e = map(int, input().split())
    s -= 1
    e -= 1
    t = C - 1
    if t < 0:
        t = 0
    elif t > N:
        t = N
    groups[t].append((idx, s, e))
    queries.append(0)

for idx, s, e in groups[0]:
    d = dist[s][e]
    if d >= INF:
        queries[idx] = -1
    else:
        queries[idx] = d

for k in range(N):
    dk = dist[k]

    for i in range(N):
        di = dist[i]
        ik = di[k]
        if ik >= INF:
            continue

        base = ik
        for j in range(N):
            v = base + dk[j]
            if v < di[j]:
                di[j] = v

    for idx, s, e in groups[k + 1]:
        d = dist[s][e]
        if d >= INF:
            queries[idx] = -1
        else:
            queries[idx] = d

for x in queries:
    print(x)
