import sys
input = sys.stdin.readline
INF = int(1e9)
from collections import deque

def Bellman_ford(start):
    xx=0
    global flag
    dist[start] = 0
    for i in range(V):
        for j in range(E): ## a->b
            node_a = edge[j][0]
            node_b = edge[j][1]
            cost = edge[j][2]

            if dist[node_a]!=INF and dist[node_b] > dist[node_a] + cost:
                dist[node_b] = dist[node_a] + cost

                if i==V-1:
                    if flag==0:
                        flag = can_return(node_b)
                    xx=1
    if xx==1:
        return True
    return False

def can_return(node):
    visit[0] = 1
    q = deque()
    q.append(0)
    while (q):
        i = q.popleft()
        for j in graph[i]:
            if visit[j] == 0:
                visit[j] = 1
                q.append(j)

    if visit[node]==1:
        return 1

T = int(input())
for x in range(T):
    flag = 0

    V,E = map(int,input().split())

    visit = [0]*V

    edge = []
    graph = [[] for i in range(V)]
    dist = [INF]*(V+1)

    for i in range(E):
        a,b,c = map(int,input().split())
        graph[b].append(a)
        edge.append((a,b,c))

    minus_cycle = Bellman_ford(0)

    if minus_cycle and flag==1:
        print("Case #%d: possible"%(x+1))
    else:
        print("Case #%d: not possible" % (x + 1))