import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs():
    global q,ma

    while(q):

        x,y = q.popleft()
        #print(array[x][y])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=N or nx<0 or ny>=M or ny<0:
                continue
            if array[nx][ny]!=0 and array[nx][ny]<=array[x][y]+1:
                continue
            array[nx][ny] = array[x][y]+1
            ma = array[nx][ny]
            q.append((nx,ny))


M,N = map(int,input().split())

array = []
for i in range(N):
    array.append(list(map(int,input().split())))

q = deque()

ma = -1
for i in range(N):
    for j in range(M):
        if array[i][j]==1:
            q.append((i,j))
        ma = max(ma,array[i][j])
bfs()
flag = 0

for i in range(N):
    for j in range(M):
        if array[i][j]==0:
            flag = 1

if flag==1 or ma==-1:
    print(-1)
else:
    print(ma-1)