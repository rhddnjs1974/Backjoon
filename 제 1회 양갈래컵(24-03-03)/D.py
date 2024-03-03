import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################

N, M = map(int,input().split())
start = input().rstrip()

arr = [[0]*M for i in range(N)]

dx = [1,0,-1,0]#d r u l
dy = [0,1,0,-1]


if start=="U":
    y_s = M//2
    y_e = M-1
    x_s = 0
    x_e = N-1
    now_go = 0
    now_num = 1
    last_num = (1+(M//2))*N

    x= x_s
    y= y_s
    while(True):
        arr[x][y] = now_num
        if now_num == last_num:
            break
        nx = dx[now_go]+x
        ny = dy[now_go]+y

        if nx<x_s or nx>x_e or ny<y_s or ny>y_e or arr[nx][ny]!=0:
            now_go = (now_go+1)%4
            continue

        x = nx
        y = ny
        now_num +=1


    for i in range(x_s,x_e+1):
        for j in range(0,y_s):
            arr[i][j] = arr[i][M-1-j]

if start=="D":
    y_s = 0
    y_e = M//2
    x_s = 0
    x_e = N-1
    now_go = 2
    now_num = 1
    last_num = (1+(M//2))*N

    x= x_e
    y= y_e
    while(True):
        arr[x][y] = now_num
        if now_num == last_num:
            break
        nx = dx[now_go]+x
        ny = dy[now_go]+y

        if nx<x_s or nx>x_e or ny<y_s or ny>y_e or arr[nx][ny]!=0:
            now_go = (now_go+1)%4
            continue

        x = nx
        y = ny
        now_num +=1


    for i in range(x_s,x_e+1):
        for j in range(y_e+1,M):
            arr[i][j] = arr[i][M-1-j]

if start=="L":
    y_s = 0
    y_e = M-1
    x_s = 0
    x_e = N//2
    now_go = 1
    now_num = 1
    last_num = (1+(N//2))*M

    x= x_e
    y= y_s
    while(True):
        arr[x][y] = now_num
        if now_num == last_num:
            break
        nx = dx[now_go]+x
        ny = dy[now_go]+y

        if nx<x_s or nx>x_e or ny<y_s or ny>y_e or arr[nx][ny]!=0:
            now_go = (now_go+1)%4
            continue

        x = nx
        y = ny
        now_num +=1


    for i in range(x_e+1,N):
        for j in range(0,M):
            arr[i][j] = arr[N-1-i][j]

if start=="R":
    y_s = 0
    y_e = M-1
    x_s = N//2
    x_e = N-1
    now_go = 3
    now_num = 1
    last_num = (1+(N//2))*M

    x= x_s
    y= y_e
    while(True):
        arr[x][y] = now_num
        if now_num == last_num:
            break
        nx = dx[now_go]+x
        ny = dy[now_go]+y

        if nx<x_s or nx>x_e or ny<y_s or ny>y_e or arr[nx][ny]!=0:
            now_go = (now_go+1)%4
            continue

        x = nx
        y = ny
        now_num +=1


    for i in range(0,x_s):
        for j in range(0,M):
            arr[i][j] = arr[N-1-i][j]


for i in arr:
    print(*i)