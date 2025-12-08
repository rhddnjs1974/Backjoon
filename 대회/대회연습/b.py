t = int(input())

for _ in range(t):
    n = int(input())
    if n%2==0:
        print(-1)
        continue
    arr = []
    for i in range(1,n+1,2):
        arr.append(i)
    for i in range(2,n,2):
        arr.append(i)
    print(*arr)