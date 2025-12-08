import sys
input = sys.stdin.readline
from collections import deque
import copy

def numberloaf(arr,N,M):#N 세로 M 가로 #덩어리 개수 세주는 함수
    num = 0
    array = copy.deepcopy(arr)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(N):
        for j in range(M):
            if array[i][j]!=0:
                num+=1
                q = deque()
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for T in range(4):
                        nx = x+dx[T]
                        ny = y+dy[T]
                        if nx<0 or ny<0 or nx>=N or ny>=M:
                            continue
                        if array[nx][ny]!=0:
                            array[nx][ny] = 0
                            q.append((nx,ny))
    return num

def calculate_melt(arr,N,M):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    array = [[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                continue
            for a in range(4):
                ni = i+dx[a]
                nj = j+dy[a]
                if ni<0 or nj<0 or ni>=N or nj>=M:
                    continue
                if arr[ni][nj]==0:
                    array[i][j] += 1
    
    return array

N, M = map(int,input().split())


ans = 0
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

if numberloaf(arr,N,M)>1:
    print(0)
else:

    for x in range(1,501):
        meltarr = calculate_melt(arr,N,M)

        for i in range(N):
            for j in range(M):
                t = arr[i][j] - meltarr[i][j]
                if t<0:
                    t=0
                arr[i][j] = t

        num = numberloaf(arr,N,M)

        if num>1:
            ans = x
            break

    print(ans)