import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
k = int(input())
tp = [0]*(k+1)
lx = [0]*(k+1)
ly = [0]*(k+1)
rx = [0]*(k+1)
ry = [0]*(k+1)

for _ in range(k):
    b,x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        tp[b] = 1
        lx[b] = x1
        rx[b] = x2
        ly[b] = min(y1,y2)
        ry[b] = max(y1,y2)
    else:
        tp[b] = 0
        lx[b] = min(x1,x2)
        rx[b] = max(x1,x2)
        ly[b] = y1
        ry[b] = y2
        
sx,sy,dx,dy = map(int,input().split())

adj = [[] for _ in range(k+1)]
for i in range(1,k+1):
    for j in range(i+1,k+1):
        if tp[i] == 0 and tp[j] == 0:
            if ly[i] == ly[j] and max(lx[i],lx[j]) <= min(rx[i],rx[j]):
                adj[i].append(j)
                adj[j].append(i)
        elif tp[i] == 1 and tp[j] == 1:
            if lx[i] == lx[j] and max(ly[i],ly[j]) <= min(ry[i],ry[j]):
                adj[i].append(j)
                adj[j].append(i)
        else:
            if tp[i] == 1:
                vx = lx[i]
                vy1 = ly[i]
                vy2 = ry[i]
                hx1 = lx[j]
                hx2 = rx[j]
                hy = ly[j]
            else:
                vx = lx[j]
                vy1 = ly[j]
                vy2 = ry[j]
                hx1 = lx[i]
                hx2 = rx[i]
                hy = ly[i]
                
            if hx1 <= vx <= hx2 and vy1 <= hy <= vy2:
                adj[i].append(j)
                adj[j].append(i)

dist = [-1]*(k+1)
dq = deque()
for i in range(1,k+1):
    if tp[i] == 0:
        if ly[i] == sy and lx[i] <= sx <= rx[i]:
            dist[i] = 1
            dq.append(i)
    else:
        if lx[i] == sx and ly[i] <= sy <= ry[i]:
            dist[i] = 1
            dq.append(i)

ans = -1
while dq:
    u = dq.popleft()
    if tp[u] == 0:
        if ly[u] == dy and lx[u] <= dx <= rx[u]:
            hit = 1
        else:
            hit = 0
    else:
        if lx[u] == dx and ly[u] <= dy <= ry[u]:
            hit = 1
        else:
            hit = 0
    
    if hit==1:
        ans = dist[u]
        break
    for v in adj[u]:
        if dist[v] < 0:
            dist[v] = dist[u]+1
            dq.append(v)

print(ans)