import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bt(x,y):
    global ans
    now.append(arr[x][y])
    alpha[ord(arr[x][y])-65] = 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or nx>=R or ny<0 or ny>=C:
            continue
        if alpha[ord(arr[nx][ny])-65]==0:
            bt(nx,ny)
    ans = max(ans,len(now))
    now.pop()
    alpha[ord(arr[x][y])-65] = 0

R,C = map(int,input().split())
arr = []
for i in range(R):
    arr.append(input().rstrip())

alpha = [0]*26
ans = 0
now = []
bt(0,0)
print(ans)