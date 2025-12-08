import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    visit[v] = 1
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        for dx in move:
            j = i + dx
            if j<=0 or j>N:
                continue
            if visit[j]==0 or visit[j]>visit[i]+1:
                visit[j] = visit[i]+1
                q.append(j)
                if j==G:
                    return visit[j]
            
    return 0

F,S,G,U,D = map(int,input().split())
#N:정점개수 / M:간선개수 / V:탐색시작번호

N = F

move = [U,-D]


visit = [0]*(N+1)
if S==G:
    print(0)
else:
    ans = bfs(S)

    if ans==0:
        print("use the stairs")
    else:
        print(ans-1)