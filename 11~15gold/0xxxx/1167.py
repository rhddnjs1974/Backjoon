import sys
input = sys.stdin.readline
from collections import deque
########################################

def bfs(v):
    visit = [1e10] * (N + 1)
    visit[v] = 0
    q = deque()
    q.append(v)
    while(q):
        x = q.popleft()
        for a,b in graph[x]:
            if visit[a]>visit[x]+b:
                visit[a] = visit[x]+b
                q.append(a)

    ma = 0
    index = 0
    for i in range(1,N+1):
        if visit[i]==1e10:
            continue

        if visit[i]>ma:
            ma = visit[i]
            index = i

    return (ma,index)
N = int(input())

graph = [[] for i in range(N+1)]
for i in range(N):
    arr = list(map(int,input().split()))
    v = arr[0]
    for i in range(1,len(arr)-1,2):
        a=arr[i]
        b=arr[i+1]
        graph[v].append((a,b))


t = bfs(1)[1]
print(bfs(t)[0])

