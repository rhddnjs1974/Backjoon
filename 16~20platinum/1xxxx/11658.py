import sys
input = sys.stdin.readline

def update(x,y,dif):
    while(x<=N):
        y1 = y
        while(y1<=N):
            fenwick[x][y1] += dif
            y1 += (y1 & -y1)
        x += (x & -x)

def subsum(x,y):
    ans = 0
    while(x>0):
        y1 = y
        while(y1>0):
            ans += fenwick[x][y1]
            y1 -= (y1 & -y1)
        x -= (x & -x)
    return ans

N,M = map(int,input().split())

arr = [[0 for i in range(N+1)]]
fenwick = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(1,N+1):
    arr.append([0]+list(map(int,input().split())))

    for j in range(1,N+1):
        update(i,j,arr[i][j])



for i in range(M):
    w,*what = map(int,input().split())
    if w==0:
        x,y,c = what
        update(x,y,c-arr[x][y])
        arr[x][y] = c
    else:
        x1,y1,x2,y2 = what
        realans = ( subsum(x2,y2)-subsum(x1-1,y2)-subsum(x2,y1-1)+subsum(x1-1,y1-1) )
        print(realans)