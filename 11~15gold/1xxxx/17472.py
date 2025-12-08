import sys
input = sys.stdin.readline
from collections import deque
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#####################################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(a,b):
    global num
    array[a][b] = num
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=N or nx<0 or ny>=M or ny<0:
                continue
            if array[nx][ny]==-1:
                array[nx][ny] = num
                q.append((nx,ny))


N,M = map(int,input().split())
edge = []

array = []
for i in range(N):
    array.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if array[i][j]==1:
            array[i][j]=-1

num = 0
for i in range(N):
    for j in range(M):
        if array[i][j]==-1:
            num+=1
            bfs(i,j)



for i in range(N):
    for j in range(M):
        if array[i][j]!=0:
            nx = i
            ny = j
            t = -1
            dest = 0
            while(nx>=0 and ny>=0 and nx<N and ny<M):
                if t>-1 and array[nx][ny]!=0:
                    dest = array[nx][ny]
                    break
                nx-=1
                t+=1
            if t>1 and array[i][j]!=dest and dest!=0:
                edge.append((t,array[i][j],dest))
            nx = i
            ny = j
            t = -1
            dest = 0
            while (nx >= 0 and ny >= 0 and nx < N and ny < M):
                if t > -1 and array[nx][ny] != 0:
                    dest = array[nx][ny]
                    break
                nx += 1
                t += 1
            if t>1 and array[i][j]!=dest and dest!=0:
                edge.append((t, array[i][j], dest))
            nx = i
            ny = j
            t = -1
            dest = 0
            while (nx >= 0 and ny >= 0 and nx < N and ny < M):
                if t > -1 and array[nx][ny] != 0:
                    dest = array[nx][ny]
                    break
                ny -= 1
                t += 1
            if t>1 and array[i][j]!=dest and dest!=0:
                edge.append((t, array[i][j], dest))
            nx = i
            ny = j
            t = -1
            dest = 0
            while (nx >= 0 and ny >= 0 and nx < N and ny < M):
                if t > -1 and array[nx][ny] != 0:
                    dest = array[nx][ny]
                    break
                ny += 1
                t += 1
            if t>1 and array[i][j]!=dest and dest!=0:
                edge.append((t, array[i][j], dest))


parent = [0] * (num + 1)
for i in range(1, num + 1):
    parent[i] = i

edge.sort()
ans = 0

bridge = 0

for cost,x,y in edge:
    if find(x)!=find(y):
        ans+=cost
        union(x,y)
        bridge+=1
if bridge==num-1:
    print(ans)
else:
    print(-1)