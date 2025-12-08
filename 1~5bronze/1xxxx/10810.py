n,m = map(int,input().split())

arr=[0]*n
for a in range(m):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        arr[x] = k
print(*arr)