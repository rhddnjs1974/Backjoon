import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b,dif):
    global N
    num = 1
    visit[a][b] = 1
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0:
                continue
            if visit[nx][ny]==0 and abs(array[x][y]-array[nx][ny])<=dif:
                visit[nx][ny] = 1
                q.append((nx,ny))
                num+=1
    return num

N = int(input())

array = []
for i in range(N):
    x = list(map(int,input().split()))
    array.append([])
    for j in x:
        array[i].append(int(j))
        
        
def check(dif):
    
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                t = bfs(i,j,dif)
                if t >= (N*N+1)//2:
                    return True
    return False


mi = 0
ma = 1000000
while(mi<=ma):
    mid = (mi+ma)//2
    visit = [[0]*N for i in range(N)]
    if check(mid):
        ma = mid-1
    else:
        mi = mid+1

print(mi)