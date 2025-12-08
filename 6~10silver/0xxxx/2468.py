import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b):
    space[a][b] = 1
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0:
                continue
            if space[nx][ny]==0:
                space[nx][ny] = 1
                q.append((nx,ny))
    return

N = int(input())

array = []
for i in range(N):
    array.append(list(map(int,input().split())))

realans = 0
for h in range(0,101):
    space = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if array[i][j]<=h:
                space[i][j] = 1
    
    ans = 0
    for i in range(N):
        for j in range(N):
            if space[i][j]==0:
                bfs(i,j)
                ans+=1
    realans = max(realans,ans)

print(realans)