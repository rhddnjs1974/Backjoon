import sys
input = sys.stdin.readline

N = int(input())
g = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

W = [0] + list(map(int, input().split()))
totalW = 0
for i in range(1, N + 1):
    totalW += W[i]

parent = [0] * (N + 1)
depth = [0] * (N + 1)
order = []

stack = [1]
parent[1] = -1
depth[1] = 0

while stack:
    u = stack.pop()
    order.append(u)
    for v in g[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        depth[v] = depth[u] + 1
        stack.append(v)

subW = [0] * (N + 1)
F1 = 0

for i in range(1, N + 1):
    F1 += W[i] * depth[i]

for u in range(N - 1, -1, -1):
    x = order[u]
    s = W[x]
    for y in g[x]:
        if y == parent[x]:
            continue
        s += subW[y]
    subW[x] = s

dp = [0] * (N + 1)
dp[1] = F1

for i in range(1, N):
    v = order[i]
    u = parent[v]
    dp[v] = dp[u] + totalW - 2 * subW[v]

ans = dp[1]
for i in range(2, N + 1):
    if dp[i] > ans:
        ans = dp[i]

print(ans)
