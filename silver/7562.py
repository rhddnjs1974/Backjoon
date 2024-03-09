import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
def bfs(a,b):
    global N,k,l
    q = deque()
    q.append((a,b))
    array[a][b] = 0
    while(q):
        x,y = q.popleft()

        if x==k and y==l:
            return array[x][y]

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0:
                continue
            if array[nx][ny]==0:
                q.append((nx,ny))
                array[nx][ny]=array[x][y]+1




T = int(input())
for i in range(T):
    N = int(input())
    array = [[0]*N for i in range(N)]
    i,j = map(int,input().split())
    k,l = map(int,input().split())
    print(bfs(i,j))