import sys
input = sys.stdin.readline
import heapq

def daik(node,dist):
    heap = [(dist,node)]
    while(heap):
        d, n = heapq.heappop(heap)
        if dp[n] < d:
            continue
        for next,w in graph[n]:
            if dp[next] > d+w:
                dp[next] = d+w
                heapq.heappush(heap,(d+w,next))


V,e = map(int,input().split())
k = int(input())
dp = [1e9]*(V+1)
dp[k] = 0
graph = [[] for i in range(V+1)]
for i in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

daik(k,0)
for i in range(1,V+1):
    if dp[i]==1e9:
        print("INF")
    else:
        print(dp[i])
