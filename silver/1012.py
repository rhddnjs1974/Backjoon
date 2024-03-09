import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b):
    global N
    array[a][b] = 0
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=M or nx<0 or ny>=N or ny<0:
                continue
            if array[nx][ny]==1:
                array[nx][ny] = 0
                q.append((nx,ny))


T = int(input())
for i in range(T):
    M,N,K = map(int,input().split())

    array = [[0]*N for i in range(M)]
    for i in range(K):
        x,y = map(int,input().split())
        array[x][y] = 1

    group = 0

    for i in range(M):
        for j in range(N):
            if array[i][j]==1:
                bfs(i,j)
                group+=1

    print(group)