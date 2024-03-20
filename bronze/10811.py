n,m = map(int,input().split())
arr=[0]
for i in range(1,n+1):
    arr.append(i)

for i in range(m):
    a,b = map(int,input().split())
    arr2=[]
    for j in arr[a:b+1]:
        arr2.append(j)
    arr2.reverse()
    for j in range(b-a+1):
        arr[j+a] = arr2[j]


print(*arr[1:])