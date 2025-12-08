n,m = map(int,input().split())
arr=[0]
for i in range(1,n+1):
    arr.append(i)

for i in range(m):
    a,b = map(int,input().split())
    arr[a],arr[b] = arr[b],arr[a]

print(*arr[1:])