import sys
input = sys.stdin.readline
from collections import deque
########################################
flag = 0
ans = -100
def bfs(v):
    global K
    global flag,ans
    visit[v] = 0
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()


        if visit[i] == ans+10:
            return
        if i==K:
            if ans==-100:
                ans = visit[i]


        j = i-1
        if 0<=j<150000 and j==K:
            flag+=1
        if 0<=j<150000 and visit[j]==0:

            visit[j] = visit[i]+1
            q.append(j)

        j = i+1
        if 0<=j<150000 and j==K:
            flag+=1
        if  0<=j<150000 and visit[j]==0:

            visit[j] = visit[i]+1
            q.append(j)

        j = i*2
        if 0<=j<150000 and j==K:
            flag+=1
        if 0<=j<150000 and visit[j]==0:

            visit[j] = visit[i]+1
            q.append(j)



N,K = map(int,input().split())
visit = [0]*150001

bfs(N)
print(ans)
print(flag)