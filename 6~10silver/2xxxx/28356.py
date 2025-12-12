n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append([0]*m)
if n==m==1:
    print(1)
    print(1)
elif n==1 or m==1:
    print(2)
    if n==1:
        for i in range(m):
            arr[0][i]=(i%2)+1
    else:
        for i in range(n):
            arr[i][0] =(i%2)+1
    for i in arr:
        print(*i)
else:
    print(4)
    for i in range(n):
        for j in range(m):
            arr[i][j] = (j%2)+1 + 2*(i%2)
    for i in arr:
        print(*i)