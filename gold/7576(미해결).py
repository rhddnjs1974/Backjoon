import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b):
    global N
    num = 1
    array[a][b] = 0
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0:
                continue
            if array[nx][ny]==1:
                array[nx][ny] = 0
                q.append((nx,ny))
                num+=1
    return num

M,N = map(int,input().split())

array = []
for i in range(N):
    array.append(list(map(int,input().split())))



for i in range(N):
    for j in range(N):
        if array[i][j]==1:
            danzi.append(bfs(i,j))

print(len(danzi))
danzi.sort()
for i in danzi:
    print(i)