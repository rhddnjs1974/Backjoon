import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    visit[v] = 0

    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()

        if 2*i<=200000 and visit[2*i]>visit[i]:
            visit[2*i] = visit[i]
            q.append(2*i)

        if i+1<=K and visit[i+1]>visit[i]+1:
            visit[i+1] = visit[i]+1
            q.append(i+1)

        if i>0 and visit[i-1]>visit[i]+1:
            visit[i-1] = visit[i]+1
            q.append(i-1)

N,K = map(int,input().split())


visit = [1e9]*(200001)

bfs(N)
print(visit[K])
