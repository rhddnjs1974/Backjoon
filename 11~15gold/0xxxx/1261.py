import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dijkstra(a,b):
    heap = []
    heapq.heappush(heap,(0,a,b))
    distance[a][b] = 0
    while heap:
        dist, x,y = heapq.heappop(heap)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if array[nx][ny]=="1":
                cost = dist+1
            else:
                cost = dist

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(heap,(cost,nx,ny))

M,N = map(int,input().split())

array = []
for i in range(N):
    array.append(input())

distance = [[INF] * (M) for i in range(N)]


dijkstra(0,0)

print(distance[N-1][M-1])