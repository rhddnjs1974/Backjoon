import sys
input = sys.stdin.readline
INF = int(1e9)

def Bellman_ford(start):
    dist[start] = 0
    for i in range(V):
        for j in range(E): ## a->b
            node_a = edge[j][0]
            node_b = edge[j][1]
            cost = edge[j][2]

            if dist[node_a]!=INF and dist[node_b] > dist[node_a] + cost:
                dist[node_b] = dist[node_a] + cost

                if i==V-1:
                    return True
    return False


V,E = map(int,input().split())

edge = []
dist = [INF]*(V+1)

for i in range(E):
    a,b,c = map(int,input().split())
    edge.append((a,b,c))

minus_cycle = Bellman_ford(1)

if minus_cycle:
    print(-1)
else:
    for i in range(2,V+1):
        if dist[i]==INF:
            print(-1)
        else:
            print(dist[i])