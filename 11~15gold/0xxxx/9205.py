import sys
input = sys.stdin.readline
from collections import deque
import itertools

t= int(input())

def bfs(v):
    visit[v] = 1
    q = deque()
    q.append(v)
    while(q):
        i = q.popleft()
        for j in graph[i]:
            if visit[j]==0:
                visit[j] = 1
                q.append(j)



for _ in range(t):
    N = int(input())
    #N:정점개수 / M:간선개수 / V:탐색시작번호
    
    graph = [[] for i in range(N+2)]
    arr = []

    for i in range(N+2):
        a,b = map(int,input().split())
        arr.append((a,b))
    
    visit = [0]*(N+2)
    
    for x,y in itertools.combinations(range(N+2),2):
        if abs(arr[x][0] - arr[y][0]) + abs(arr[x][1] - arr[y][1])<=1000:
            graph[x].append(y)
            graph[y].append(x)
    
    bfs(0)
    if visit[N+1]==1:
        print("happy")
    else:
        print("sad")