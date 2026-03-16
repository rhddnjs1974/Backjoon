n = int(input())

arr = [[0]*500 for i in range(500)]

for i in range(n):
    a,b,c,d = map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            arr[x][y] = 1

ans=0
for i in range(500):
    for j in range(500):
        ans+=arr[i][j]
print(ans)