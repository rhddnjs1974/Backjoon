import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
a = [input().strip() for _ in range(n)]

g = [[-1]*m for _ in range(n)]
sz = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if a[i][j] == '0' and g[i][j] == -1:
            q = deque()
            q.append((i,j))
            g[i][j] = len(sz)
            cnt = 1
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if a[nx][ny] == '0' and g[nx][ny] == -1:
                            g[nx][ny] = g[i][j]
                            cnt += 1
                            q.append((nx,ny))
            sz.append(cnt)

for i in range(n):
    s = ''
    for j in range(m):
        if a[i][j] == '0':
            s += '0'
        else:
            v1 = -1
            v2 = -1
            v3 = -1
            v4 = -1
            now = 1
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if 0 <= ni < n and 0 <= nj < m and a[ni][nj] == '0':
                    t = g[ni][nj]
                    if t != v1 and t != v2 and t != v3 and t != v4:
                        now += sz[t]
                        if v1 == -1:
                            v1 = t
                        elif v2 == -1:
                            v2 = t
                        elif v3 == -1:
                            v3 = t
                        else:
                            v4 = t
            s += str(now%10)
    print(s)