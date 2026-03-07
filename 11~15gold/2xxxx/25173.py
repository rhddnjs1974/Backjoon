import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            ax, ay = i, j
            row[j] = 0
        elif row[j] == 3:
            bx, by = i, j
            row[j] = 0
    arr.append(row)

a, d, b, e = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(4):
    if bx+dx[i] == ax and by+dy[i] == ay:
        bd = i
        break
ad = bd

def find(x, y, d):
    v = [[0] * m for _ in range(n)]
    v[x][y] = 1
    c = 1
    s = 1
    nd = d
    while c < n*m:
        for _ in range(2):
            for _ in range(s):
                x += dx[nd]
                y += dy[nd]
                if 0 <= x < n and 0 <= y < m and v[x][y] == 0:
                    v[x][y] = 1
                    c += 1
                    if arr[x][y] == 1:
                        return x, y
                if c == n*m:
                    break
            nd = (nd+1) % 4
        s += 1
    return -1, -1

def dmg(sx, sy):
    q = deque([(sx, sy)])
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        if x == ax and y == ay:
            if dist[x][y] < e:
                return e-dist[x][y]
            return 0
        
        if dist[x][y] == e-1:
            continue
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            if nx == bx and ny == by:
                continue
            
            if (nx != ax or ny != ay) and arr[nx][ny] == 1:
                continue
            
            if dist[nx][ny] != -1:
                continue
            
            dist[nx][ny] = dist[x][y]+1
            q.append((nx, ny))
    return 0

while True:
    b -= d
    if b <= 0:
        print("VICTORY!")
        exit()

    px = ax
    py = ay
    moved = 0
    for _ in range(4):
        nx = ax+dx[ad]
        ny = ay+dy[ad]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and (nx != bx or ny != by):
            ax, ay = nx, ny
            moved = 1
            break
        ad = (ad+1) % 4
        a -= 1
        
        if a <= 0:
            print("CAVELIFE...")
            exit()

    sx, sy = find(bx, by, bd)
    if sx != -1:
        a -= dmg(sx, sy)
        
        if a <= 0:
            print("CAVELIFE...")
            exit()

    if moved == 1:
        bx, by = px, py
        bd = ad