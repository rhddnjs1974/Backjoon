from collections import deque

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