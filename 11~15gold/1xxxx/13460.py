import sys
input = sys.stdin.readline
from collections import deque
########################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(b_x,b_y,r_x,r_y,num):
    global N
    num = 1
    q = deque()
    q.append((b_x,b_y,r_x,r_y,num))
    flag = 0
    while(q):
        b_x,b_y,r_x,r_y,num = q.popleft()

        for i in range(4):
            b_nx,b_ny,r_nx,r_ny = b_x,b_y,r_x,r_y
            if i==0: #오른쪽
                while(arr[b_nx][b_ny+1]=="."):
                    b_ny+=1
                if arr[b_nx][b_ny+1]=="O":
                    continue

                while (arr[r_nx][r_ny + 1] == "."):
                    r_ny += 1
                if arr[r_nx][r_ny + 1] == "O":

                    flag = 1
                    break

                if r_nx==b_nx and r_ny==b_ny:
                    if b_y>r_y:
                        r_ny-=1
                    else:
                        b_ny-=1
                q.append((b_nx,b_ny,r_nx,r_ny,num+1))

            if i==1: #왼쪽
                while(arr[b_nx][b_ny-1]=="."):
                    b_ny-=1
                if arr[b_nx][b_ny-1]=="O":
                    continue

                while (arr[r_nx][r_ny - 1] == "."):
                    r_ny -= 1
                if arr[r_nx][r_ny - 1] == "O":
                    flag = 1
                    break

                if r_nx==b_nx and r_ny==b_ny:
                    if b_y>r_y:
                        b_ny+=1
                    else:
                        r_ny+=1
                q.append((b_nx,b_ny,r_nx,r_ny,num+1))

            if i==2: #아래쪽
                while(arr[b_nx+1][b_ny]=="."):
                    b_nx+=1
                if arr[b_nx+1][b_ny]=="O":
                    continue

                while (arr[r_nx+1][r_ny] == "."):
                    r_nx += 1
                if arr[r_nx+1][r_ny] == "O":
                    flag = 1
                    break

                if r_nx==b_nx and r_ny==b_ny:
                    if b_x>r_x:
                        r_nx-=1
                    else:
                        b_nx-=1
                q.append((b_nx,b_ny,r_nx,r_ny,num+1))

            if i==3: #위쪽
                while(arr[b_nx-1][b_ny]=="."):
                    b_nx-=1
                if arr[b_nx-1][b_ny]=="O":
                    continue

                while (arr[r_nx-1][r_ny] == "."):
                    r_nx -= 1
                if arr[r_nx-1][r_ny] == "O":
                    flag = 1
                    break

                if r_nx==b_nx and r_ny==b_ny:
                    if b_x>r_x:
                        b_nx+=1
                    else:
                        r_nx+=1
                q.append((b_nx,b_ny,r_nx,r_ny,num+1))

        if flag==1:
            return num
        if num==11:
            return -1

n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(input().rstrip()))


for i in range(n):
    for j in range(m):
        if arr[i][j]=="B":
            arr[i][j] = "."
            B_x = i
            B_y = j
        if arr[i][j] == "R":
            arr[i][j] = "."
            R_x = i
            R_y = j
        if arr[i][j] == "O":
            O_x = i
            O_y = j

print(bfs(B_x,B_y,R_x,R_y,0))