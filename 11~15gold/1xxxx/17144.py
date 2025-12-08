import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
arr = []
for i in range(R):
    arr.append(list(map(int,input().split())))
    
cur = []
cleaner = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]
a = 0
b = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]>0:
            cur.append((i,j,arr[i][j]))
        if arr[i][j]==-1:
            if a==0:
                a=i
            else:
                b=i

for _ in range(T):
    while cur:
        x,y,v = cur.pop()
        c = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue
            if (nx,ny)==(a,0) or (nx,ny)==(b,0):
                continue
            arr[nx][ny]+=v//5
            c+=1
        arr[x][y] -= (v//5)*c
    
    ##
    x = a
    y = 1
    i = 1
    t = 0
    while True:
        nx = x+dx[i]
        ny = y+dy[i]
        if nx==R or ny==C or nx==-1 or ny==-1:
            i = (i-1)%4
            continue
        if x==a and y==0:
            break
        arr[x][y], t = t, arr[x][y]
        x,y = nx,ny
    
    x = b
    y = 1
    i = 1
    t = 0
    while True:
        nx = x+dx[i]
        ny = y+dy[i]
        if nx==R or ny==C or nx==-1 or ny==-1:
            i = (i+1)%4
            continue
        if x==b and y==0:
            break
        arr[x][y], t = t, arr[x][y]
        x,y = nx,ny
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]>0:
                cur.append((i,j,arr[i][j]))

print(sum(cur[i][2] for i in range(len(cur))))