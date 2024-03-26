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

            if dist[node_b] > dist[node_a] + cost:
                dist[node_b] = dist[node_a] + cost

                if i==V-1:
                    return True
    return False

T = int(input())

for i in range(T):
    V,M,W = map(int,input().split())

    edge = []
    dist = [INF]*(V+1)
    E = 2*M+W
    for i in range(M):
        a,b,c = map(int,input().split())
        edge.append((a,b,c))
        edge.append((b, a, c))

    for i in range(W):
        a,b,c = map(int,input().split())
        edge.append((a,b,-c))

    minus_cycle = Bellman_ford(1)


    if minus_cycle:
        print("YES")
    else:
        print("NO")