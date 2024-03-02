import sys
input = sys.stdin.readline
from itertools import combinations, permutations

def count():
    ma = 0
    x=1
    for i in range(n):
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                x+=1
            else:
                x=1
            ma = max(x,ma)
        x=1
    x=1
    for j in range(n):
        for i in range(n-1):
            if arr[i][j] == arr[i+1][j]:
                x+=1
            else:
                x=1
            ma = max(x,ma)
        x=1

    return ma

n = int(input())
arr=[]
for i in range(n):
    x = input().rstrip()
    arr.append([])
    for j in x:
        arr[i].append(j)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0

for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx<0 or nx>= n or ny<0 or ny>= n:
                continue

            arr[nx][ny], arr[i][j] = arr[i][j], arr[nx][ny]
            ans = max(ans,count())
            arr[nx][ny], arr[i][j] = arr[i][j], arr[nx][ny]

print(ans)