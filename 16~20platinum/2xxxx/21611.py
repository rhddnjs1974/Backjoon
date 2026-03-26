import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

path = []
x = n//2
y = n//2
step = 1
while len(path) < (n*n-1):
    for _ in range(step):
        y -= 1
        path.append((x, y))
        
    for _ in range(step):
        x += 1
        path.append((x, y))
        
    step += 1
    
    for _ in range(step):
        y += 1
        path.append((x, y))
        
    for _ in range(step):
        x -= 1
        path.append((x, y))
        
    step += 1

idx = [[-1]*n for _ in range(n)]

for i in range(n*n-1):
    x, y = path[i]
    idx[x][y] = i

arr = []
for i in range(n*n-1):
    x, y = path[i]
    if board[x][y] != 0:
        arr.append(board[x][y])

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

ans = 0

for _ in range(m):
    d, s = map(int, input().split())

    for k in range(1, s+1):
        nx = (n//2)+dx[d]*k
        ny = (n//2)+dy[d]*k
        t = idx[nx][ny]
        if t < len(arr):
            arr[t] = 0

    nxt = []
    for v in arr:
        if v != 0:
            nxt.append(v)
    arr = nxt

    while True:
        nxt = []
        boom = False
        i = 0
        while i < len(arr):
            j = i+1
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
            cnt = j-i
            if cnt >= 4:
                ans += arr[i] * cnt
                boom = True
            else:
                for k in range(i, j):
                    nxt.append(arr[k])
            i = j
            
        arr = nxt
        if not boom:
            break

    nxt = []
    i = 0
    limit = n*n-1
    while i < len(arr) and len(nxt) < limit:
        j = i+1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        nxt.append(j-i)
        if len(nxt) == limit:
            break
        nxt.append(arr[i])
        i = j
        
    if len(nxt) > limit:
        nxt = nxt[:limit]
    arr = nxt

print(ans)