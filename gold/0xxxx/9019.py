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

        i = str(i)
        i = "0"*(4-len(i))+i

        if int(i)==K:
            return

        j = (int(i)*2)%10000
        if visit[j]==0:
            visit[j] = visit[int(i)]+1
            dic[j]=(i,"D")
            q.append(j)

        j = (int(i)-1)%10000
        if visit[j]==0:
            visit[j] = visit[int(i)]+1
            dic[j]=(i,"S")
            q.append(j)

        j = i[1]+i[2]+i[3]+i[0]
        j = int(j)
        if visit[j]==0:
            visit[j] = visit[int(i)]+1
            dic[j]=(i,"L")
            q.append(j)

        j = i[3] + i[0] + i[1] + i[2]
        j = int(j)
        if visit[j] == 0:
            visit[j] = visit[int(i)] + 1
            dic[j] = (i, "R")
            q.append(j)

T = int(input())
for i in range(T):
    N,K = map(int,input().split())
    visit = [0]*10001

    dic={}

    bfs(N)

    now = K
    ans= []
    while(now!=N):
        ans.append(dic[now][1])
        now = int(dic[now][0])
    ans.reverse()
    for i in ans:
        print(i,end="")
    print()