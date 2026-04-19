import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())

if N == 1:
    print(1)
    print(1)
    exit()

diffs = [A]
if B != A:
    diffs.append(B)

nbr = [[] for _ in range(N+1)]
eid = [[] for _ in range(N+1)]
edge_cnt = 0
for d in diffs:
    for x in range(1, N-d+1):
        nbr[x].append(x+d)
        eid[x].append(edge_cnt)
        nbr[x+d].append(x)
        eid[x+d].append(edge_cnt)
        edge_cnt += 1

if edge_cnt == 0:
    print(-1)
    exit()

for v in range(1, N+1):
    if len(nbr[v]) == 0:
        print(-1)
        exit()

visited = [False] * (N+1)
visited[1] = True
stack = [1]
cnt = 1
while stack:
    v = stack.pop()
    for u in nbr[v]:
        if not visited[u]:
            visited[u] = True
            cnt += 1
            stack.append(u)

if cnt != N:
    print(-1)
    exit()

odd = []
for v in range(1, N+1):
    if len(nbr[v]) % 2 == 1:
        odd.append(v)

if len(odd) != 0 and len(odd) != 2:
    print(-1)
    exit()

if len(odd) == 2:
    start = odd[0]
else:
    start = 1

used = [False] * edge_cnt
it = [0] * (N+1)
stack = [start]
path = []
while stack:
    v = stack[-1]
    while it[v] < len(nbr[v]) and used[eid[v][it[v]]]:
        it[v] += 1
    if it[v] < len(nbr[v]):
        u = nbr[v][it[v]]
        used[eid[v][it[v]]] = True
        it[v] += 1
        stack.append(u)
    else:
        path.append(v)
        stack.pop()

path.reverse()
print(len(path))
for x in path:
    print(x, end=" ")
print()
