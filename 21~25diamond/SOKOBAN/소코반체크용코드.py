import heapq
import sys
from collections import deque
input = sys.stdin.readline

INF = 10**18

n,m = map(int,input().split())
g = [list(input().rstrip()) for _ in range(n)]

wall = [[False for _ in range(m)] for _ in range(n)]
br = -1
bc = -1
sr = -1
sc = -1
pr = -1
pc = -1

for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            wall[i][j] = True
        elif g[i][j] == 'P':
            pr = i
            pc = j
        elif g[i][j] == 'B':
            if br == -1:
                br = i
                bc = j
            else:
                br = min(br, i)
                bc = min(bc, j)
        elif g[i][j] == 'S':
            if sr == -1:
                sr = i
                sc = j
            else:
                sr = min(sr, i)
                sc = min(sc, j)

bid = [[-1 for _ in range(m)] for _ in range(n)]
pos = []

for i in range(n-1):
    for j in range(m-1):
        ok = True
        for di in range(2):
            for dj in range(2):
                if wall[i+di][j+dj]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            bid[i][j] = len(pos)
            pos.append((i, j))

sb = -1
gb = -1
if 0 <= br < n-1 and 0 <= bc < m-1:
    sb = bid[br][bc]
if 0 <= sr < n-1 and 0 <= sc < m-1:
    gb = bid[sr][sc]

if sb == -1 or gb == -1:
    print(-1)
    exit()

anchors = []
valid = []
mp = []
nxt = []

for i in range(len(pos)):
    r,c = pos[i]
    arr = [
        (r, c-1),
        (r+1, c-1),
        (r, c+2),
        (r+1, c+2),
        (r-1, c),
        (r-1, c+1),
        (r+2, c),
        (r+2, c+1)
    ]
    anchors.append(arr)

    v = [False for _ in range(8)]
    d = dict()
    for k in range(8):
        x,y = arr[k]
        if 0 <= x < n and 0 <= y < m and not wall[x][y]:
            v[k] = True
            d[x*m+y] = k
    valid.append(v)
    mp.append(d)

    go = [-1 for _ in range(8)]
    for k in range(8):
        nr = r
        nc = c
        if k == 0 or k == 1:
            nc += 1
        elif k == 2 or k == 3:
            nc -= 1
        elif k == 4 or k == 5:
            nr += 1
        else:
            nr -= 1
        if 0 <= nr < n-1 and 0 <= nc < m-1:
            go[k] = bid[nr][nc]
    nxt.append(go)

seen = [0 for _ in range(n * m)]
dist = [0 for _ in range(n * m)]
stamp = 0
cache = dict()

def bfs(x, y, b):
    global stamp
    key = (x, y, b)
    if key in cache:
        return cache[key]

    ret = [-1 for _ in range(8)]
    r,c = pos[b]

    if not (0 <= x < n and 0 <= y < m):
        cache[key] = ret
        return ret
    if wall[x][y]:
        cache[key] = ret
        return ret
    if r <= x <= r+1 and c <= y <= c+1:
        cache[key] = ret
        return ret

    need = 0
    for k in range(8):
        if valid[b][k]:
            need += 1

    stamp += 1
    q = deque()
    idx = x*m+y
    seen[idx] = stamp
    dist[idx] = 0
    q.append((x, y))
    found = 0

    while q:
        x,y = q.popleft()
        idx = x*m+y

        if idx in mp[b]:
            k = mp[b][idx]
            if ret[k] == -1:
                ret[k] = dist[idx]
                found += 1
                if found == need:
                    break

        nx = x-1
        ny = y
        if nx >= 0 and not wall[nx][ny]:
            if not (r <= nx <= r+1 and c <= ny <= c+1):
                nidx = nx*m+ny
                if seen[nidx] != stamp:
                    seen[nidx] = stamp
                    dist[nidx] = dist[idx]+1
                    q.append((nx, ny))

        nx = x+1
        ny = y
        if nx < n and not wall[nx][ny]:
            if not (r <= nx <= r+1 and c <= ny <= c+1):
                nidx = nx*m+ny
                if seen[nidx] != stamp:
                    seen[nidx] = stamp
                    dist[nidx] = dist[idx]+1
                    q.append((nx, ny))

        nx = x
        ny = y-1
        if ny >= 0 and not wall[nx][ny]:
            if not (r <= nx <= r+1 and c <= ny <= c+1):
                nidx = nx*m+ny
                if seen[nidx] != stamp:
                    seen[nidx] = stamp
                    dist[nidx] = dist[idx]+1
                    q.append((nx, ny))

        nx = x
        ny = y+1
        if ny < m and not wall[nx][ny]:
            if not (r <= nx <= r+1 and c <= ny <= c+1):
                nidx = nx*m+ny
                if seen[nidx] != stamp:
                    seen[nidx] = stamp
                    dist[nidx] = dist[idx]+1
                    q.append((nx, ny))

    cache[key] = ret
    return ret

if sb == gb:
    print(0)
    exit()

d = [[INF for _ in range(8)] for _ in range(len(pos))]
pq = []

start = bfs(pr, pc, sb)
for k in range(8):
    if start[k] != -1:
        d[sb][k] = start[k]
        heapq.heappush(pq, (start[k], sb, k))

while len(pq) > 0:
    cur,b,k = heapq.heappop(pq)
    if cur != d[b][k]:
        continue
    if b == gb:
        print(cur)
        exit()

    x,y = anchors[b][k]
    move = bfs(x, y, b)

    for nk in range(8):
        if move[nk] == -1:
            continue
        nb = nxt[b][nk]
        if nb == -1:
            continue
        nd = cur+move[nk]+1
        if nd < d[nb][nk]:
            d[nb][nk] = nd
            heapq.heappush(pq, (nd, nb, nk))

print(-1)