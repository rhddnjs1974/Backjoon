import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = []
s_arr = [[0]*(N+1) for i in range(N+1)]

for i in range(N):
    arr.append(list(map(int,input().split())))

s_arr[1][1] = arr[0][0]

for i in range(N):
    if i!=0:
        s_arr[i+1][1] = s_arr[i][1] + arr[i][0]
    for j in range(1,N):
        s_arr[i+1][j+1] = s_arr[i+1][j] + s_arr[i][j+1] - s_arr[i][j] + arr[i][j]


for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(s_arr[x2][y2]-s_arr[x2][y1-1]-s_arr[x1-1][y2]+s_arr[x1-1][y1-1])