import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs():
    visit[1] = 1
    q = deque()
    q.append(1)
    while(q):
        i = q.popleft()
        for j in range(1,7):
            if i+j>100:
                continue
            k = i+j
            if move[k]!=0:
                k = move[k]
            if visit[k]!=0 and visit[k]<=visit[i]+1:
                continue


            visit[k] = visit[i]+1
            q.append(k)

N,M = map(int,input().split())

move = [0]*101

for i in range(N+M):
    a,b = map(int,input().split())
    move[a] = b


visit = [0]*(101)

bfs()
print(visit[100]-1)
