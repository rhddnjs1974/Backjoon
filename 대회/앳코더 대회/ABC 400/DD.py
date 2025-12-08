from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1; B -= 1; C -= 1; D -= 1

INF = 10**9
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

dq = deque()
dq.append((A, B))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if S[nx][ny] == '.':
                if dist[nx][ny] > dist[x][y]:
                    dist[nx][ny] = dist[x][y]
                    dq.appendleft((nx, ny))
            else:
                if dist[nx][ny] > dist[x][y]+1:
                    dist[nx][ny] = dist[x][y]+1
                    dq.append((nx,ny))
                nx = nx + dx[i]
                ny = ny + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if dist[nx][ny] > dist[x][y]+1:
                        dist[nx][ny] = dist[x][y]+1
                        dq.append((nx,ny))


#for i in dist:
#    print(i)
print(dist[C][D])
