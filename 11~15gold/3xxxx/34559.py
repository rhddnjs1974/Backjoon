import sys
input = sys.stdin.readline

def prefix(arr): #2차원
    x = len(arr)
    y = len(arr[0])
    s_arr = [[0]*(y+1) for i in range(x+1)]
    for i in range(x):
        for j in range(y):
            s_arr[i+1][j+1] = s_arr[i+1][j] + s_arr[i][j+1] - s_arr[i][j] + arr[i][j]
    
    return s_arr # 행렬 각 첫번째 0 한줄 추가된 상태

def range_sum(parr,startx,starty,lastx,lasty): #2차원 구간합 계산
    return parr[lastx][lasty]-parr[lastx][starty-1]-parr[startx-1][lasty]+parr[startx-1][starty-1]


n,m = map(int,input().split())
arr = [[0]*m for i in range(n)]
for i in range(n):
    A = input().rstrip()
    for x in range(m):
        arr[i][x] = int(A[x])+1

q = [(0,0)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
while q:
    x,y = q.pop()
    arr[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if arr[nx][ny]==1:
            q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            arr[i][j]=1

pre = prefix(arr)

q = int(input())
for i in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    t = range_sum(pre,r1,c1,r2,c2)
    if t==0:
        print("Yes")
    else:
        print("No",t)