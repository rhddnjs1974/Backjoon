import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
############################################
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dijkstra():
    heap = []
    heapq.heappush(heap,(0,0,0))
    distance[0][0] = 0
    while heap:
        dist, x,y = heapq.heappop(heap)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            cost = dist + array[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(heap,(cost,nx,ny))

numb = 0
while(True):
    numb += 1
    N = int(input())
    if N==0:
        break

    distance = [[INF] * (N) for i in range(N)]

    array = []
    for i in range(N):
        array.append(list(map(int,input().split())))

    dijkstra()

    print("Problem %d: %d"%(numb,distance[N-1][N-1]+array[0][0]))