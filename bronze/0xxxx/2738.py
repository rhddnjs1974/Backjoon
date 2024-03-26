n,m = map(int,input().split())

arr = [[0]*m for i in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        arr[i][j]+=a[j]
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(m):
        arr[i][j]+=a[j]
for i in arr:
    print(*i)