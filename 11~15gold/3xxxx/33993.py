n,r,c,w = map(int,input().split())

arr = [[0]*(c+31) for i in range(r+31)]
for i in range(n):
    x,y = map(int,input().split())
    arr[x+15][y+15] = 1

prearr = [[0]*(c+31) for i in range(r+31)]
for i in range(1,r+31):
    for j in range(1,c+31):
        prearr[i][j] = arr[i][j] + prearr[i-1][j] + prearr[i][j-1] - prearr[i-1][j-1]


t = w//2
ans = 0
for i in range(16-t,r+16-t):
    for j in range(16-t,c+16-t):
        if arr[i+t][j+t]==1:
            continue
        now = prearr[i+w-1][j+w-1]-prearr[i-1][j+w-1]-prearr[i+w-1][j-1]+prearr[i-1][j-1]
        if now>ans:
            ans = now
            ansx = i+t
            ansy = j+t

print(ans)
print(ansx-15, ansy-15)
