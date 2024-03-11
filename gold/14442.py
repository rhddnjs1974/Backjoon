import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    global N
    q = deque()
    q.append((0,0,0)) #0,0 / 벽부순횟수 0
    visit[0][0][0] = 1
    while(q):
        bk,x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=M or ny<0:
                continue
            if array[nx][ny]==0 and visit[bk][nx][ny] > visit[bk][x][y]+1:
                visit[bk][nx][ny] = visit[bk][x][y]+1
                q.append((bk,nx,ny))
            if array[nx][ny]==1 and bk<K and visit[bk+1][nx][ny] > visit[bk][x][y]+1:
                visit[bk+1][nx][ny] = visit[bk][x][y] + 1
                q.append((bk+1, nx, ny))

N,M,K = map(int,input().split())

array = []
for i in range(N):
    x = input().rstrip()
    array.append([])
    for j in x:
        array[i].append(int(j))

visit = [[[1000001]*M for i in range(N)] for j in range(K+1)]


bfs()

T = 1000001
for i in range(K+1):
    T = min (visit[i][N-1][M-1],T)
if T==1000001:
    print(-1)
else:
    print(T)