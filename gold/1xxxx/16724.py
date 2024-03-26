import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x,y):
    visit[x][y] = 1
    if arr[x][y]=="D":
        nx = x+1
        ny = y
        if nx<0 or nx>=n or ny<0 or ny>=m:
            return
        union(x * m + y, nx * m + ny)
        if visit[nx][ny]==0:

            dfs(nx,ny)

    elif arr[x][y] == "U":
        nx = x - 1
        ny = y
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return
        union(x * m + y, nx * m + ny)
        if visit[nx][ny] == 0:

            dfs(nx, ny)

    elif arr[x][y] == "R":
        nx = x
        ny = y+1
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return
        union(x * m + y, nx * m + ny)
        if visit[nx][ny] == 0:

            dfs(nx, ny)

    elif arr[x][y] == "L":
        nx = x
        ny = y-1
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return
        union(x * m + y, nx * m + ny)
        if visit[nx][ny] == 0:

            dfs(nx, ny)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n*m)

for i in range(n*m):
    parent[i] = i

arr = []
for i in range(n):
    arr.append(input())

visit = [[0]*(m) for i in range(n)]
for i in range(n):
    for j in range(m):
        if visit[i][j]==0:
            dfs(i,j)


ans = set()
for i in range(n*m):
    ans.add(find(i))
print(len(ans))