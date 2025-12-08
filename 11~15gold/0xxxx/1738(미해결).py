import sys
input = sys.stdin.readline
INF = int(1e9)

# 틀린 부분
# 음수 사이클에서 도착지로 갈 수 있는 길 있는지 확인해야함
# 갈 수 있으면 -1 / 아니면 경로 출력

def Bellman_ford(start):
    dist[start] = 0

    for i in range(V):
        for j in range(E): ## a->b
            node_a = edge[j][0]
            node_b = edge[j][1]
            cost = edge[j][2]

            if dist[node_a]!=INF and dist[node_b] > dist[node_a] + cost:
                dist[node_b] = dist[node_a] + cost
                route[node_b] = node_a

                if i==V-1 and node_b==V:
                    return True
    return False



V,E = map(int,input().split())

route = [0 for i in range(V+1)]

edge = []
dist = [INF]*(V+1)

for i in range(E):
    a,b,c = map(int,input().split())
    edge.append((a,b,-c))

minus_cycle = Bellman_ford(1)
arr = [V]
if minus_cycle:
    print(-1)
else:
    x = V
    while(x!=1):
        x = route[x]
        arr.append(x)

    arr.reverse()
    print(*arr)