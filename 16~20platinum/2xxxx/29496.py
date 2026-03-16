import sys
import heapq

input = sys.stdin.readline

n = int(input())

for a in range(n, 1, -1):
    m = a * (a-1) // 2
    x = n-m
    if x < 0:
        continue
    if a%2 == 1:
        if x == 1:
            continue
    else:
        if x < a // 2:
            continue
    break


if a%2 == 1:
    d = [0]*a
    i = 0
    for _ in range(2*x,0,-2):
        d[i] += 2
        i += 1
        if i == a:
            i = 0
else:
    d = [1]*a
    i = 0
    for _ in range(2*x-a,0,-2):
        d[i] += 2
        i += 1
        if i == a:
            i = 0

heap = []
for i in range(a):
    if d[i] > 0:
        heapq.heappush(heap, (-d[i], i))

arr = []

while heap:
    p1, v1 = heapq.heappop(heap)
    p2, v2 = heapq.heappop(heap)
    p1 = -p1
    p2 = -p2
    arr.append((v1, v2))
    p1 -= 1
    p2 -= 1
    if p1 > 0:
        heapq.heappush(heap, (-p1, v1))
    if p2 > 0:
        heapq.heappush(heap, (-p2, v2))

graph = [[] for _ in range(a)]
use = []
eid = 0

for i in range(a):
    for j in range(i+1, a):
        graph[i].append((j, eid))
        graph[j].append((i, eid))
        use.append(0)
        eid += 1

for u, v in arr:
    graph[u].append((v, eid))
    graph[v].append((u, eid))
    use.append(0)
    eid += 1

itarr = [0] * a
starr = [0]
ans = []

while starr:
    v = starr[-1]
    while itarr[v] < len(graph[v]) and use[graph[v][itarr[v]][1]] == 1:
        itarr[v] += 1
        
    if itarr[v] == len(graph[v]):
        ans.append(v)
        starr.pop()
        
    else:
        ne, idx = graph[v][itarr[v]]
        use[idx] = 1
        starr.append(ne)

ans.reverse()

print(a)
for i in range(n):
    print(ans[i]+1, end=' ')
print()