import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
arr = []
r,c, d = map(int,input().split())

for i in range(N):
    arr.append(list(map(int,input().split())))

ans = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
while(True):

    if arr[r][c]==0:
        arr[r][c]=2
        ans+=1
    
    flag = 0
    for i in range(4):
        nr = dx[i] + r
        nc = dy[i] + c

        if nr<0 or nc<0 or nr>=N or nc>=M:
            continue
        if arr[nr][nc]==0:
            flag=1

            break
    
    if flag==0:
        nr = r - dx[d]
        nc = c - dy[d]
        if nr<0 or nc<0 or nr>=N or nc>=M:
            break
        else:
            if arr[nr][nc]==1:
                break
            else:
                r = nr
                c = nc
                continue
    else:
        while(True):
            d = (d-1)%4
            nr = r + dx[d]
            nc = c + dy[d]
            if nr<0 or nc<0 or nr>=N or nc>=M:
                continue
            if arr[nr][nc]==0:
                r = nr
                c = nc
                break

print(ans)