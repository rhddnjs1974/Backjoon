import sys
from collections import deque
input = sys.stdin.readline

def add(u,v,t):
    to.append(v)
    ok.append(t)
    nxt.append(head[u])
    head[u] = len(to)-1

n,m = map(int,input().split())

head = [-1]*(n+1)
to = []
nxt = []
ok = []

for i in range(m):
    u,v = map(int,input().split())
    add(u,v,1)
    add(v,u,0)

INF = 10**20
dist = [INF]*(3*(n+1))
q = deque()

dist[3] = 0
dist[4] = 1
dist[5] = 1
q.append(3)
q.append(4)
q.append(5)

while q:
    s = q.popleft()
    d = dist[s]
    u = s//3
    mode = s%3
    
    e = head[u]

    if mode == 0:
        while e != -1:
            v = to[e]
            base = v*3
            if ok[e] == 1 and d < dist[base]:
                dist[base] = d
                q.appendleft(base)
                
            nd = d+1
            if nd < dist[base+2]:
                dist[base+2] = nd
                q.append(base+2)
                
            e = nxt[e]
            
    elif mode == 1:
        while e != -1:
            v = to[e]
            base = v*3
            if d < dist[base]:
                dist[base] = d
                q.appendleft(base)
                
            nd = d+1
            if nd < dist[base+1]:
                dist[base+1] = nd
                q.append(base+1)
                
            if nd < dist[base+2]:
                dist[base+2] = nd
                q.append(base+2)
                
            e = nxt[e]
            
    else:
        while e != -1:
            v = to[e]
            base = v*3
            nd = d+1
            
            if nd < dist[base+2]:
                dist[base+2] = nd
                q.append(base+2)
                
            e = nxt[e]

ans = min(dist[n*3], dist[n*3+1], dist[n*3+2])

if ans == INF:
    print(-1)
else:
    print(ans)