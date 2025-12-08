import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs1(x,y):
    visit1[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if arr1[nx][ny]==0:
            continue
        if visit1[nx][ny]==1:
            continue
        if arr1[nx][ny] == arr1[x][y]:
            dfs1(nx,ny)

def dfs2(x,y):
    visit2[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if arr2[nx][ny]==0:
            continue
        if visit2[nx][ny]==1:
            continue
        if arr2[nx][ny] == arr2[x][y]:
            dfs2(nx,ny)

N = int(input())
arr = []
for i in range(N):
    arr.append(input().rstrip())
    
arr1 = []
arr2 = []
visit1 = []
visit2 = []

for i in range(N):
    arr1.append([])
    arr2.append([])
    visit1.append([])
    visit2.append([])
    for j in arr[i]:
        visit1[i].append(0)
        visit2[i].append(0)
        if j=="R":
            arr1[i].append(1)
            arr2[i].append(1)
        elif j=="G":
            arr1[i].append(2)
            arr2[i].append(1)
        else:
            arr1[i].append(3)
            arr2[i].append(2)

ans1=0
ans2=0

for i in range(N):
    for j in range(N):
        if visit1[i][j]==0:
            ans1+=1
            dfs1(i,j)
for i in range(N):
    for j in range(N):
        if visit2[i][j]==0:
            ans2+=1
            dfs2(i,j)
            
print(ans1,ans2)