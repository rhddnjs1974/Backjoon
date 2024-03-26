import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    visit[v] = 0
    global ans,ans2

    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()

        if 2*i<=200000 and visit[2*i]>=visit[i]+1:
            visit[2*i] = visit[i]+1
            if 2 * i == K:
                if visit[2*i]<ans:
                    ans = visit[2*i]
                    ans2 = 1
                elif visit[2*i]==ans:
                    ans2+=1
            q.append(2*i)

        if i+1<=K and visit[i+1]>=visit[i]+1:
            visit[i+1] = visit[i]+1
            if i+1 == K:
                if visit[i+1]<ans:
                    ans = visit[i+1]
                    ans2 = 1
                elif visit[i+1]==ans:
                    ans2+=1
            q.append(i+1)

        if i>0 and visit[i-1]>=visit[i]+1:
            visit[i-1] = visit[i]+1
            if i-1 == K:
                if visit[i-1]<ans:
                    ans = visit[i-1]
                    ans2 = 1
                elif visit[i-1]==ans:
                    ans2+=1
            q.append(i-1)

N,K = map(int,input().split())
ans = 1e9
ans2 = 0

visit = [1e9]*(200001)

if N==K:
    print(0)
    print(1)
else:
    bfs(N)
    print(ans)
    print(ans2)
