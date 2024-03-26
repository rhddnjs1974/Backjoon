import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    global K
    visit[v] = 0
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        if i==K:
            print(visit[i])
            return

        j = i-1
        if 0<=j<150000 and visit[j]==0:
            visit[j] = visit[i]+1
            q.append(j)

        j = i+1
        if  0<=j<150000 and visit[j]==0:
            visit[j] = visit[i]+1
            q.append(j)

        j = i*2
        if 0<=j<150000 and visit[j]==0:
                visit[j] = visit[i]+1
                q.append(j)

N,K = map(int,input().split())
visit = [0]*150001

bfs(N)
