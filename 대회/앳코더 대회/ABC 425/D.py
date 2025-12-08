import sys
input = sys.stdin.readline
from collections import deque

H,W=map(int,input().split())
SS = []
for i in range(H):
    SS.append(input().rstrip())

S = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        S[i][j] = SS[i][j]

q = deque()
blacknei = [[0]*W for i in range(H)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        for a in range(4):
            nx = i+dx[a]
            ny = j+dy[a]
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if S[nx][ny]=="#":
                blacknei[i][j] += 1

q = []
for i in range(H):
    for j in range(W):
        if blacknei[i][j]==1:
            q.append((i,j))
            
while (q):
    now = []
    for a,b in q:
        S[a][b]="#"
            
    for a,b in q:
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if S[nx][ny]=="#":
                continue
            blacknei[nx][ny] += 1
            if blacknei[nx][ny]==1:
                now.append((nx,ny))
    
    q = []
    for a,b in now:
        if blacknei[a][b]==1:
            q.append((a,b))

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            ans+=1
            
print(ans)