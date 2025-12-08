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
        for j in graph[i]:
            if visit[j]==-1:
                visit[j] = 1-visit[i]
                q.append(j)
            else:
                if visit[j]==visit[i]:
                    return False
    return True


T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    #N:정점개수 / M:간선개수

    graph = [[] for i in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)


    visit = [-1]*(N+1)

    flag = 0
    for i in range(1,N+1):
        if visit[i]==-1:
            if bfs(i)==False:
                flag = 1

    if flag==0:
        print("YES")
    else:
        print("NO")