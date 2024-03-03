import sys
input = sys.stdin.readline
from itertools import combinations, permutations
###################################################
from collections import deque

def bfs(start):
    global U
    global T
    queue = deque([(start,U)])
    visit[start] = 1
    while queue:
        x = queue.popleft()
        v = x[0]
        time = x[1]
        for i in graph[v]:
            if not visit[i]:
                if v!=1:
                    if len(graph[v])==2:
                        queue.append((i,time))
                        visit[i] = visit[v]+time
                    else:
                        queue.append((i, time+T))
                        visit[i] = visit[v] + time+T
                else:
                    if len(graph[v])==1:
                        queue.append((i,time))
                        visit[i] = visit[v]+time
                    else:
                        queue.append((i, time+T))
                        visit[i] = visit[v] + time+T

def dfs(start):
    global move
    global real_move
    visit2[start]=1
    move +=1
    real_move = move
    for node in graph[start]:
        if visit2[node]==0:
            real_move = move
            dfs(node)
            move += 1


D, N, U, T = map(int,input().split())

broke = []
for i in range(N):
    broke.append(list(map(int,input().split())))

graph = [[] for i in range(2**D)]

for i in range(1,2**D):
    if i!=1:
        if [i//2,i] not in broke:
            graph[i].append(i//2)
    if i*2+1<=2**D-1:
        if [i, i*2] not in broke:
            graph[i].append(i*2)
        if [i, i*2+1] not in broke:
            graph[i].append(i*2+1)

visit = [0] * (2**D)

visit2 = [0] * (2**D)

bfs(1)


twin = max(visit)-1

move = -1
real_move = 0
dfs(1)

poni = (real_move)*U

if twin>poni:
    print(":blob_twintail_sad:")
elif twin<poni:
    print(":blob_twintail_aww:")
else:
    print(":blob_twintail_thinking:")
