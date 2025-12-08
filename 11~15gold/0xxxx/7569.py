import sys
input = sys.stdin.readline
from collections import deque
########################################
dh = [0,0,0,0,1,-1]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
def bfs():
    global q,ma

    while(q):

        h,x,y = q.popleft()
        #print(array[x][y])
        for i in range(6):
            nh = h+dh[i]
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=N or nx<0 or ny>=M or ny<0 or nh>=H or nh<0:
                continue
            if array[nh][nx][ny]!=0 and array[nh][nx][ny]<=array[h][x][y]+1:
                continue
            array[nh][nx][ny] = array[h][x][y]+1
            ma = array[nh][nx][ny]
            q.append((nh,nx,ny))


M,N,H = map(int,input().split())

array = []
for k in range(H):
    array.append([])
    for i in range(N):
        array[k].append(list(map(int,input().split())))

q = deque()

ma = -1
for k in range(H):
    for i in range(N):
        for j in range(M):
            if array[k][i][j]==1:
                q.append((k,i,j))
            ma = max(ma,array[k][i][j])
bfs()
flag = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if array[k][i][j]==0:
                flag = 1

if flag==1 or ma==-1:
    print(-1)
else:
    print(ma-1)