import sys
input = sys.stdin.readline
from collections import deque

arr = []
H,W = map(int,input().split())
for i in range(H):
    S = input().rstrip()
    arr.append([])
    for xx in range(len(S)):
        x = S[xx]
        if x=="T":
            tx = i
            ty = xx
        if x=="." or x=="T":
            arr[-1].append(0)
        else:
            arr[-1].append(1)

pres = [[0]*(W+1) for i in range(H+1)]

for i in range(1,H+1):
    for j in range(1,W+1):
        pres[i][j] = pres[i-1][j] + pres[i][j-1] - pres[i-1][j-1] + arr[i-1][j-1]

visit = set()
q = deque()
q.append((0,0,0,0,0,0,0))
visit.add((0,0,0,0,0,0))

ddy = [-1,1,0,0]
ddx = [0,0,-1,1]
ans = 0
while q:
    dx,dy,kl,kr,ku,kd,dist = q.popleft()
    flag= 0
    for i in range(4):
        nx = dx + ddx[i]
        ny = dy + ddy[i]
        nl,nr,nu,nd = kl,kr,ku,kd
        if i==0:
            nu = max(ku,-ny)
        if i==1:
            nd = max(nd,ny)
        if i==2:
            nl = max(kl,-nx)
        if i==3:
            nr = max(kr,nx)
        
        r1 = nu
        r2 = H-1-nd
        c1 = nl
        c2 = W-1-nr
        if r1>r2 or c1>c2:
            flag = 1
            ans = dist
            break
        
        if 0<=tx-ny<H and 0<=ty-nx<W and arr[tx-ny][ty-nx] and (r1<=tx-ny<=r2) and (c1<=ty-nx<=c2):
            continue
        
        if pres[r2+1][c2+1]-pres[r1][c2+1]-pres[r2+1][c1]+pres[r1][c1]==0:
            flag = 1
            ans = dist
            break
        
        tt = (nx,ny,nl,nr,nu,nd)
        if tt not in visit:
            visit.add(tt)
            q.append((nx,ny,nl,nr,nu,nd,dist+1))    
    
    if flag==1:
        break

if flag==0:
    print(-1)
else:
    print(ans+1)