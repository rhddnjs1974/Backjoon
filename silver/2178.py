import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b):
    global N,M
    array[a][b] = 2
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=M or ny<0:
                continue
            if array[nx][ny]==1:
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))


N,M = map(int,input().split())

array = []
for i in range(N):
    x = input().rstrip()
    array.append([])
    for j in x:
        array[i].append(int(j))



bfs(0,0)

print(array[N-1][M-1]-1)