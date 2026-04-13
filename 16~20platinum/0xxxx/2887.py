import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True

n = int(input())
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []
for dim in range(3):
    planets.sort(key=lambda p: p[dim])
    for i in range(n-1):
        cost = abs(planets[i][dim]-planets[i+1][dim])
        edges.append((cost, planets[i][3], planets[i+1][3]))

edges.sort()
parent = list(range(n))
rank = [0] * n
ans = 0
cnt = 0
for c, a, b in edges:
    if union(a, b):
        ans += c
        cnt += 1
        if cnt == n-1:
            break

print(ans)
