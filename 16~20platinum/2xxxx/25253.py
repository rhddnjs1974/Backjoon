import sys
input = sys.stdin.readline

n, m = map(int, input().split())
V = m * m

adj = [[[]for i in range(V)] for j in range(m + 1)]

for x in range(1, m + 1):
    for y in range(1, m + 1):
        for z in range(1, m + 1):
            val = int(input())
            adj[val][(x-1)*m + (y-1)].append((y-1)*m + (z-1))

arr = list(map(int, input().split()))

for start in range(V):
    cur = [0] * V
    cur[start] = 1
    alive = 1

    for lab in arr:
        nxt = [0] * V
        lists = adj[lab]
        any_new = 0

        for v in range(V):
            if cur[v]:
                for u in lists[v]:
                    if nxt[u]==0:
                        nxt[u] = 1
                        any_new = 1

        if any_new==0:
            alive = 0
            break

        cur = nxt

    if alive and cur[start]:
        print("yes")
        exit()

print("no")

